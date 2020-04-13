# Generated by go2rpm 1
%bcond_without check

# https://github.com/digitalautonomy/wahay
%global goipath         github.com/digitalautonomy/wahay
%global commit          971d012c63c4c1220e8e082a63f02ec0e16c382a

%gometa

%global common_description %{expand:
An easy-to-use, secure and decentralized conference call application}

%global golicenses      COPYING LICENSE
%global godocs          DEVELOPER.md CONTRIBUTORS README.md\\\

Name:           wahay
Version:        0
Release:        0.4%{?dist}
Summary:        An easy-to-use, secure and decentralized conference call application (this repository is a mirror of an internal work repository)

License:        GPL-3.0-only
# FIXME: Upstream uses unknown SPDX tag GPL-3.0-only!
URL:            %{gourl}
Source0:        %{gosource}

Requires: mumble, tor >= 0.3.5, gtk3, xclip

BuildRequires:  desktop-file-utils
BuildRequires:  golang(github.com/atotto/clipboard)
BuildRequires:  golang(github.com/coyim/gotk3adapter/gdka)
BuildRequires:  golang(github.com/coyim/gotk3adapter/gdki)
BuildRequires:  golang(github.com/coyim/gotk3adapter/gliba)
BuildRequires:  golang(github.com/coyim/gotk3adapter/glibi)
BuildRequires:  golang(github.com/coyim/gotk3adapter/gtka)
BuildRequires:  golang(github.com/coyim/gotk3adapter/gtki)
BuildRequires:  golang(github.com/cubiest/jibberjabber)
BuildRequires:  golang(github.com/digitalautonomy/grumble/pkg/logtarget)
BuildRequires:  golang(github.com/digitalautonomy/grumble/server)
BuildRequires:  golang(github.com/kardianos/osext)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/wybiral/torgo)
BuildRequires:  golang(golang.org/x/crypto/scrypt)
BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(golang.org/x/text/message)
BuildRequires:  golang(golang.org/x/text/message/catalog)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/coyim/gotk3adapter/glib_mock)
BuildRequires:  golang(github.com/coyim/gotk3adapter/gtk_mock)
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/wahay %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

install -d %{buildroot}/%{_mandir}/man1/
install -p packaging/ubuntu/ubuntu/usr/share/man/man1/wahay.1.gz %{buildroot}/%{_mandir}/man1/

sed "s/__NAME__/Wahay/g" gui/config_files/wahay.desktop | sed "s/__EXEC__/\/usr\/bin\/wahay/g" | sed "s/__ICON__/wahay/" | sed "s/Internet/Network/"  > %{name}.desktop

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop

for size in 192x192 256x256 512x512; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
  install -p gui/images/wahay-${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/wahay.png
done


%if %{with check}
%check
%gocheck
%endif

%files
%license COPYING LICENSE
%doc DEVELOPER.md CONTRIBUTORS README.md 
%{_mandir}/man1/wahay.*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*

%gopkgfiles

%changelog
* Mon Mar 30 14:48:00 -05 2020 rafael <rafael@autonomia.digital> - 0.0.4.20200331git971d012
- Upgrade to commit 971d012c63c4c1220e8e082a63f02ec0e16c382a
- Add gtk3 as a dependency
* Mon Mar 30 14:48:00 -05 2020 rafael <rafael@autonomia.digital> - 0.0.3.20200331git3906ea6
- Upgrade to commit 3906ea63d21872d25893e247322f0ee34d00a499
* Tue Mar 24 13:19:24 -05 2020 rafael <rafael@autonomia.digital> - 0-0.2.20200318git4abfed1
* Mon Mar 18 13:19:24 -05 2020 rafael <rafael@autonomia.digital> - 0-0.1.20200318git4abfed1
- Initial package
