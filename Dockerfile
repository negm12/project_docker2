FROM alpine

COPY os2_project.py /
RUN apk add --no-cache python3 py3-pip


CMD python3 os2_project.py