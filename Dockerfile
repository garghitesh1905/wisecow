FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd && \
    ln -s /usr/games/fortune /usr/bin/fortune && \
    ln -s /usr/games/cowsay /usr/bin/cowsay

COPY wisecow.sh /usr/local/bin/wisecow.sh
RUN chmod +x /usr/local/bin/wisecow.sh

CMD ["/usr/local/bin/wisecow.sh"]
