FROM ubuntu:18.04

ENV HOME /home/user

# Install python dependencies
RUN apt-get update \
      && apt-get install -y \
      python3 \
      python3-pyqt5

# Add local user and change to home directory
RUN adduser --quiet --disabled-password user

# Copy source code
COPY app $HOME

# Change ownership of source code
RUN chown -R user:user $HOME

# Run application
WORKDIR $HOME
CMD ["python3", "mainwindow.py"]
