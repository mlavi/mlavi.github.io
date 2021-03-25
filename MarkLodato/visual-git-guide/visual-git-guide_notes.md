- https://github.com/MarkLodato/visual-git-guide
---
https://miktex.org/howto/install-miktex-unx

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D6BC243565B2087BC3F897C9277A7293F59E4889
echo "deb http://miktex.org/download/ubuntu bionic universe" | sudo tee /etc/apt/sources.list.d/miktex.list
sudo apt-get update && sudo apt-get install miktex
sleep 60
miktexsetup finish && initexmf --set-config-value [MPM]AutoInstall=1

- update modules
- add xcolor*
- add pgf*

https://pgf-tikz.github.io/

sudo apt-get install texlive texlive-fonts-extra pdf2svg imagemagick
make
- Then make works, mostly! Generates PDFs, but not SVG...error.
---
- http://www.texample.net/tikz/
  - http://www.texample.net/media/pgf/builds/pgfmanual_3.0.1a.pdf
  - http://www.texample.net/tikz/builds/2015/08/29/a/
---
cp basic-remote-usage.tex .
cp visual-git-guide_Makefile Makefile
make && pdf2svg basic-remote-usage.pdf basic-remote-usage.svg

diff common.tex visual-git-guide_mark.tex 
12a13
> \colorlet{remote}{orange!40}
33a35
> remote/.style={index=remote},
82,84c84,88
< \newcommand\historynode[1][0,.5]{\node [history] (head) at (#1) {History};}
< \newcommand\indexnode[1][0,-1]{\node [index] (index) at (#1) {Stage (Index)};}
< \newcommand\worknode[1][0,-2.5]{\node [work] (work) at (#1) {Working Directory};}
---
> \newcommand\remotenode[1][0,.5]{\node [remote] (remote) at (#1) {Remote};}
> \newcommand\historynode[1][0,-1]{\node [history] (head) at (#1) {History};}
> \newcommand\indexnode[1][0,-2.5]{\node [index] (index) at (#1) {Stage (Index)};}
> \newcommand\worknode[1][0,-3.5]{\node [work] (work) at (#1) {Working Directory};}
> 

