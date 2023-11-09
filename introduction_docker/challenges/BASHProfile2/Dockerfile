FROM debian:bullseye-slim

COPY .bashrc /root/.bashrc
RUN groupadd -r ctf_player && useradd -r -g ctf_player ctf_player
USER ctf_player

CMD ["/bin/bash"]