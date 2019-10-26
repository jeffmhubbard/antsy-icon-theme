#
# Spec file for package antsy-icon-theme
#
# Copyright (c) 2019 Jeff M. Hubbard
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name:           antsy-icon-theme
Version:        0.1
Release:        0
License:        CC-BY-SA-4.0
Summary:        Antsy Icon theme
Url:            https://github.com/jeffmhubbard/antsy-icon-theme
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Antsy material icon theme

%prep
%setup -q
find -L . -type l -print -delete
chmod +x autogen.sh
chmod a-x README.md

%build
./autogen.sh
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
%fdupes %{buildroot}%{_datadir}/icons/Antsy

%post
%icon_theme_cache_post Antsy

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_datadir}/icons/Antsy
%ghost %{_datadir}/icons/Antsy/icon-theme.cache
