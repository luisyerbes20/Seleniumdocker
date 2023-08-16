from continuumio/miniconda3
MAINTAINER  "luis yerbes"
RUN /opt/conda/bin/conda install jupyter -y && \
    /opt/conda/bin/conda install pandas && \
    /opt/conda/bin/conda install pymysql



