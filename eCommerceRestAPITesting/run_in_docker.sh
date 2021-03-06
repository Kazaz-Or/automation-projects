
source ./env_docker.sh

DATE_WITH_TIME=`date "+%Y%m%d_%H%M%S"`

set -x
docker run --rm -it \
-v $(pwd)/web:/automation/web \
-e WC_KEY=${WC_KEY} \
-e WC_SECRET=${WC_SECRET} \
-e WP_HOST=${WP_HOST} \
-e MACHINE=${MACHINE} \
-e DB_USER=${DB_USER} \
-e DB_PASSWORD=${DB_PASSWORD} \
web_api_test \
pytest -c /automation/web/pytest.ini \
--color=yes \
--html /automation/web/reports/report_${DATE_WITH_TIME}.html \
-m "$1" /automation/web
