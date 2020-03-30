To fix: To build you need to manually clone and generate the tar.gz expected by the spec file.
Spec files uploaded to Fedora's repo auto download the source code. I would fix this later.

```
git clone https://github.com/digitalautonomy/wahay.git
mv wahay/ wahay-3906ea63d21872d25893e247322f0ee34d00a499
mv grumble/ grumble-c109af8d88b4b9cb77afe1f18572c66027cf8c0b
tar zcf wahay-3906ea63d21872d25893e247322f0ee34d00a499.tar.gz wahay-3906ea63d21872d25893e247322f0ee34d00a499
rm -rf wahay-3906ea63d21872d25893e247322f0ee34d00a499
```

To build this package you would need to install the following packages from the Fedora repos:
*  golang-github-atotto-clipboard-devel
*  golang-github-kardianos-osext-devel
*  golang-gopkg-check-1-devel

Packages build in CAD respos that are necessary to build:
*  golang-github-coyim-gotk3adapter    
*  golang-github-digitalautonomy-grumble  
*  golang-github-gotk3
*  golang-github-cubiest-jibberjabber  
*  golang-github-wybiral-torgo



Building the package:
```
fedpkg --release f31 local
```
