%define _branch 0
%define _major  1
%define _minor  0

Name:		linux-ftools
Version:	%{_branch}.%{_major}.%{_minor}
Release:	1%{?dist}
Summary:	The tools linux-fadvise and linux-fallocate

Group:		Administration/Tools
License:	Apache License 2.0
URL:		https://github.com/credativ/linux-ftools
Source0:	https://github.com/credativ/linux-ftools/archive/REL%{_branch}_%{_major}_%{_minor}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:  ppc64 x86_64
BuildRequires:  autoconf, automake, make, gcc

%description
These are tools designed for working with modern linux system calls
including, mincore, fallocate, fadvise, etc.

%prep
%setup -q -n linux-ftools-REL%{_branch}_%{_major}_%{_minor}

%build
aclocal
autoconf
automake
%configure --prefix=%{_prefix}
DESTDIR=%{buildroot} make


%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=%{buildroot} make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{_prefix}/bin/linux-fallocate
%{_prefix}/bin/linux-fadvise
%{_prefix}/bin/linux-fincore


%changelog
* Mon Sep 14 2015 Bernd Helmle <bernd.helmle@credativ.de> 0.1.0-1
- Initial package version
