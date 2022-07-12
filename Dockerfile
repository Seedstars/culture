FROM returntocorp/semgrep

ARG TEST_VERSION=${TEST_VERSION:-2022.07}

WORKDIR /app

COPY ./code/validation/${TEST_VERSION}/rules/python/* /app/
COPY ./code/validation/${TEST_VERSION}/targets/python/* /app/

ENTRYPOINT [ "semgrep" ]
CMD ["--quiet","--test", "."]
