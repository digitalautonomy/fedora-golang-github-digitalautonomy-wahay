To fix: To build you need to manually clone and generate the tar.gz expected by the spec file.
Spec files uploaded to Fedora's repo auto download the source code. I would fix this later.

```
git clone https://github.com/digitalautonomy/wahay.git
mv wahay/ wahay-971d012c63c4c1220e8e082a63f02ec0e16c382a
tar zcf wahay-971d012c63c4c1220e8e082a63f02ec0e16c382a.tar.gz wahay-971d012c63c4c1220e8e082a63f02ec0e16c382a
rm -rf wahay-971d012c63c4c1220e8e082a63f02ec0e16c382a
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
