FROM nu11secur1ty/kali-linux-docker
MAINTAINER hvqzao@gmail.com

RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list && \
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean
RUN apt-get -y install nmap masscan screen
RUN apt-get -y install git
RUN mkdir -p ~/x/p
RUN cd ~/x/p && git clone https://github.com/hvqzao/ipport

CMD ["/bin/su","-"]
