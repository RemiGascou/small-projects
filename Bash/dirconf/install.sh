#!/usr/bin/env bash

INSTALLDIR=~/.bashapps

#==============================================

echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m Creating ${INSTALLDIR}"
mkdir -p ${INSTALLDIR}/

echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m Installing .ba.dirconf"

if [[ -f "${INSTALLDIR}/.ba.dirconf" ]]; then
    rm ${INSTALLDIR}/.ba.dirconf
fi

echo "IyEvdXNyL2Jpbi9lbnYgYmFzaAoKIyA9PT09PT09PT09PT09PSBEaXJDb25mIFV0aWxzID09PT09PT09PT09PT09CiMKIwojCiMgZGlyY29uZl9pbml0ICAgIDogQ3JlYXRlcyBhIC5kaXJjb25mIGZpbGUKIyBkaXJjb25mX25lYXJlc3QgOiBMb2FkcyB0aGUgbmVhcmVzdCAuZGlyY29uZiBpbiBwYXJlbnRzCiMgZGlyY29uZl9jZCAgICAgIDogQXV0b2xvYWQgbmVhcmVzdCAuZGlyY29uZiB3aGVuIGNkCgpmdW5jdGlvbiBkaXJjb25mX2luaXQgKCkgewogICAgaWYgW1sgJDEgPT0gJy1yJyBdXTsgdGhlbgogICAgICAgIHJtIC5kaXJjb25mCiAgICBmaQogICAgaWYgW1sgLWYgIi5kaXJjb25mIiBdXTsgdGhlbgogICAgICAgIGVjaG8gLWUgIlx4MWJbMW1bXHgxYls5MW1XQVJOXHgxYlswbVx4MWJbMW1dXHgxYlswbSAuZGlyY29uZiBhbHJlYWR5IGV4aXN0cy4iCiAgICAgICAgZWNobyAtZSAiICAgICB8IFVzZSBceDFiWzFtZGlyY29uZl9pbml0IC1yXHgxYlswbSB0byByZXNldCBjb25maWd1cmF0aW9uLiIKICAgIGVsc2UKICAgICAgICBlY2hvICIjIS91c3IvYmluL2VudiBiYXNoIiA+IC5kaXJjb25mCiAgICAgICAgZWNobyAiIiA+PiAuZGlyY29uZgogICAgZmkKfQoKIwoKZnVuY3Rpb24gZGlyY29uZl9uZWFyZXN0KCkgewogICAgaWYgW1sgJCMgLWVxIDEgXV07IHRoZW4KICAgICAgICBkaXI9JDEKICAgIGVsc2UKICAgICAgICBkaXI9JChwd2QpCiAgICBmaQogICAgRk9VTkQ9MAogICAgd2hpbGUgW1sgJGRpciAhPSAnLycgJiYgJGRpciAhPSAnLicgJiYgJGRpciAhPSAnLi8nIF1dOyBkbwogICAgICAgIGlmIFtbIC1mICIkZGlyLy5kaXJjb25mIiBdXTsgdGhlbgogICAgICAgICAgICBzb3VyY2UgIiRkaXIvLmRpcmNvbmYiCiAgICAgICAgICAgIEZPVU5EPTEKICAgICAgICAgICAgYnJlYWs7CiAgICAgICAgZmkKICAgICAgICBkaXI9IiQoZGlybmFtZSAiJGRpciIpIgogICAgZG9uZQogICAgaWYgW1sgJHtGT1VORH0gLWVxIDAgXV07IHRoZW4KICAgICAgICBzb3VyY2Ugfi8uYmFzaHJjCiAgICBmaQoKfQoKIwoKZnVuY3Rpb24gZGlyY29uZl9jZCgpIHsKICAgIGNkICIkQCIgJiYgZGlyY29uZl9uZWFyZXN0Cn0KCmFsaWFzIGNkPSJkaXJjb25mX2NkIgo=" | base64 -d > ${INSTALLDIR}/.ba.dirconf

echo "" >> ~/.bashrc
echo "if [[ -f \"${INSTALLDIR}/.ba.dirconf\" ]]; then" >> ~/.bashrc
echo "  source ${INSTALLDIR}/.ba.dirconf" >> ~/.bashrc
echo "fi" >> ~/.bashrc
