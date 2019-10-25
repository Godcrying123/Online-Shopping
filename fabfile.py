import os
from datetime import datetime

from fabric.api import (
    env, run, prefix, local, settings, roles,
)
from fabric.contrib.files import exists, upload_template
from fabric.decorators import task

env.roledefs = {
    'myserver': ['root@16.186.79.97']
}
env.PROJECT_NAME = 'shopsite'
env.SETTINGS_BASE = 'shopsite/shopsite/settings/base.py'

env.DEPLOY_PATH = '/root/PycharmProjects/shopsite/venv'
env.VENV_ACTIVATE = os.path.join(env.DEPLOY_PATH, 'bin', 'activate')
env.PYPI_HOST = 'upload.pypi.org'
env.PYPI_INDEX = 'https://upload.pypi.org/legacy/'
env.PROCESS_COUNT = 2
env.PORT_PREFIX = 909


class _Version:
    origin_record = {}

    def replace(self, f, version):
        with open(f, 'r') as fd:
            origin_content = fd.read()
            content = origin_content.replace('${version}', version)

        with open(f, 'w') as fd:
            fd.write(content)

        self.origin_record[f] = origin_content

    def set(self, file_list, version):
        for f in file_list:
            self.replace(f, version)

    def revert(self):
        for f, content in self.origin_record.items():
            with open(f, 'w') as fd:
                fd.write(content)


@task
def build(version=None):
    """在本地打包并上传到PYPI上
        1. 配置版本号
        2. 打包并上传
    """
    if not version:
        version = datetime.now().strftime('%m%d%H%M%S')

    _version = _Version()
    _version.set(['setup.py', env.SETTINGS_BASE], version)

    with settings(warn_only=True):
        local('python setup.py sdist bdist_wheel')
        local('twine.exe upload dist/*')

    _version.revert()


def _ensure_virtualenv():
    if exists(env.VENV_ACTIVATE):
        return True

    if not exists(env.DEPLOY_PATH):
        run('mkdir -p %s' % env.DEPLOY_PATH)

    run('python -m venv %s' % env.DEPLOY_PATH)


def _reload_supervisoird(deploy_path, profile):
    template_dir = 'conf'
    filename = 'supervisord.conf'
    destination = env.DEPLOY_PATH
    context = {
        'process_count': env.PROCESS_COUNT,
        'port_prefix': env.PORT_PREFIX,
        'profile': profile,
    }
    upload_template(filename, destination, context=context, use_jinja=True, template_dir=template_dir)
    with settings(warn_only=True):
        result = run('supervisorctl -c %s/supervisord.conf shutdown' % deploy_path)
        if result:
            run('supervisord -c %s/supervisord.conf' % deploy_path)


@task
@roles('myserver')
def deploy(version, profile):
    """ 部署指定版本
    1. 确认虚拟环境已经配置
    2. 激活虚拟环境
    3. 安装软件包
    4. 启动
    """
    _ensure_virtualenv()
    package_name = env.PROJECT_NAME + '==' + version
    with prefix('source %s' % env.VENV_ACTIVATE):
        run('pip install %s -i %s --trusted-host %s' % (
            package_name,
            env.PYPI_INDEX,
            env.PYPI_HOST,
        ))
        _reload_supervisoird(env.DEPLOY_PATH, profile)
        run('echo yes | %s/bin/manage.py collectstatic' % env.DEPLOY_PATH)
