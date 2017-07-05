# deploy.py
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())


# WSGI applichtion
WSGI_APPLICATION = 'config.wsgi.deploy.application'


# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')


# 배포모드니까 DEBUG는 False
DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
DATABASES = config_secret_deploy['django']['databases']

print('@@@@@@ DEBUG:', DEBUG)
print('@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)


# 1. RDS 연동후 돌아가는지 확인
#    DJANGO_SETTINGS_MODULE=config.settings.deploy설정
#    createsuperuser커맨드 실행 후 pgAdmin으로 auth_user테이블에 데이터가 들어갔는지 확인

# - Custom User model
#   member app생성, AbstractUser를 상속받은 User클래스 정의, img_profile필드(ImageField)추가
#   RDS에서 데이터베이스 초기화 후 migreate 실행
#   User를 Django admin에 등록

# - 파일 업로드 관련 설정
#   MEDIA_URL, MEDIA_ROOT설정 -> debug.py, deploy.py에 각각 따로 설정 (같은 값)
#   MEDIA_ROOT는 프로젝트폴더 /.media 폴더 사용
#   이후 img_