#
# Conditional build:
%bcond_without	perl	# don't build perl bindings
%bcond_without	python	# don't build python bindings (required by prewikka)
#
%include	/usr/lib/rpm/macros.perl
Summary:	The Prelude library
Summary(pl.UTF-8):	Biblioteka Prelude
Name:		libprelude
Version:	0.9.16.2
Release:	1
License:	GPL v2 or commercial
Group:		Libraries
Source0:	http://www.prelude-ids.org/download/releases/%{name}-%{version}.tar.gz
# Source0-md5:	1dcffc4149bd444ba977c5d1d8573792
Patch0:		%{name}-libdir.patch
URL:		http://www.prelude-ids.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gnutls-devel >= 1.0.17
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libltdl-devel
BuildRequires:	libtool
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python:BuildRequires:	python-devel >= 1:2.5}
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Prelude library is a collection of generic functions providing
communication between the Prelude Hybrid IDS suite components. It
provides a convenient interface for sending alerts to Prelude Manager
with transparent SSL, failover and replication support, asynchronous
events and timer interfaces, an abstracted configuration API (hooking
at the commandline, the configuration line, or wide configuration,
available from the Manager), and a generic plugin API. It allows you
to easily turn your favorite security program into a Prelude sensor.

%description -l pl.UTF-8
Biblioteka Prelude to zbiór ogólnych funkcji zapewniających
komunikację pomiędzy komponentami zestawu Prelude Hybrid IDS.
Dostarcza wygodny interfejs do wysyłania alarmów do zarządcy Prelude z
przezroczystą obsługę SSL, failover i replikacji, interfejsy do
zdarzeń asynchronicznych i zegarów, abstrakcyjne API konfiguracyjne
(obsługujące linię poleceń, linię konfiguracji i konfigurację
dostępną z zarządcy) oraz ogólne API wtyczek. Pozwala łatwo zamienić
ulubiony program związany z bezpieczeństwem na czujnik Prelude.

%package libs
Summary:	The Prelude library
Summary(pl.UTF-8):	Biblioteka Prelude
Group:		Libraries
Requires:	gnutls >= 1.0.17
Requires:	libgcrypt >= 1.1.94

%description libs
The Prelude library.

%description libs -l pl.UTF-8
Biblioteka Prelude.

%package devel
Summary:	Header files and development documentation for libprelude
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programistyczna dla libprelude
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnutls-devel >= 1.0.17
Requires:	libgcrypt-devel >= 1.1.94
Requires:	libltdl-devel

%description devel
Header files and development documentation for libprelude.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programistyczna dla libprelude.

%package static
Summary:	Static libprelude library
Summary(pl.UTF-8):	Statyczna biblioteka libprelude
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libprelude library.

%description static -l pl.UTF-8
Statyczna biblioteka libprelude.

%package -n perl-libprelude
Summary:	libprelude Perl bindings
Summary(pl.UTF-8):	Dowiązania Perla do libprelude
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}-%{release}

%description -n perl-libprelude
libprelude Perl bindings.

%description -n perl-libprelude -l pl.UTF-8
Dowiązania Perla dla libprelude.

%package -n python-libprelude
Summary:	libprelude Python bindings
Summary(pl.UTF-8):	Dowiązania Pythona dla libprelude
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-libprelude
libprelude Python bindings.

%description -n python-libprelude -l pl.UTF-8
Dowiązania Pythona dla libprelude.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I libmissing/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--enable-gtk-doc \
	--with%{!?with_perl:out}-perl \
	--with%{!?with_python:out}-python \
	--with-html-dir=%{_gtkdocdir}/libprelude \
	--with-perl-installdirs=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.README NEWS README
%attr(755,root,root) %{_bindir}/prelude-adduser
%attr(755,root,root) %{_bindir}/prelude-admin
%dir %{_sysconfdir}/prelude
%dir %{_sysconfdir}/prelude/default
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prelude/default/*.conf
%dir %{_sysconfdir}/prelude/profile
%{_mandir}/man1/prelude-admin.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprelude.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libprelude.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libprelude-config
%attr(755,root,root) %{_libdir}/libprelude.so
%{_libdir}/libprelude.la
%{_includedir}/libprelude
%{_aclocaldir}/libprelude.m4
%{_gtkdocdir}/libprelude

%files static
%defattr(644,root,root,755)
%{_libdir}/libprelude.a

%if %{with perl}
%files -n perl-libprelude
%defattr(644,root,root,755)
%{perl_vendorarch}/Prelude.pm
%dir %{perl_vendorarch}/auto/Prelude
%{perl_vendorarch}/auto/Prelude/Prelude.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Prelude/Prelude.so
%endif

%if %{with python}
%files -n python-libprelude
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_prelude.so
%{py_sitedir}/prelude.py[co]
%{py_sitedir}/prelude-*.egg-info
%endif
