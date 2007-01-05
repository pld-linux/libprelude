%bcond_without	perl
%bcond_without	python		# required by prewikka

%include	/usr/lib/rpm/macros.perl
Summary:	The Prelude library
Summary(pl):	Biblioteka Prelude
Name:		libprelude
Version:	0.9.12
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.prelude-ids.org/download/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2e8769cd05d51d3e69380bf234e6efef
URL:		http://www.prelude-ids.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gnutls-devel >= 1.0.17
BuildRequires:	gtk-doc
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python:BuildRequires:	python-devel}
BuildRequires:	rpm-perlprov
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

%description -l pl
Biblioteka Prelude to zbiór ogólnych funkcji zapewniaj±cych
komunikacjê pomiêdzy komponentami zestawu Prelude Hybrid IDS.
Dostarcza wygodny interfejs do wysy³ania alarmów do zarz±dcy Prelude z
przezroczyst± obs³ugê SSL, failover i replikacji, interfejsy do
zdarzeñ asynchronicznych i zegarów, abstrakcyjne API konfiguracyjne
(obs³uguj±ce liniê poleceñ, liniê konfiguracji i konfiguracjê
dostêpn± z zarz±dcy) oraz ogólne API wtyczek. Pozwala ³atwo zamieniæ
ulubiony program zwi±zany z bezpieczeñstwem na czujnik Prelude.

%package libs
Summary:	The Prelude library
Summary(pl):	Biblioteka Prelude
Group:		Libraries

%description libs
The Prelude library.

%description libs -l pl
Biblioteka Prelude.

%package devel
Summary:	Header files and development documentation for libprelude
Summary(pl):	Pliki nag³ówkowe i dokumentacja programistyczna dla libprelude
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnutls-devel

%description devel
Header files and development documentation for libprelude.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programistyczna dla libprelude.

%package static
Summary:	Static libprelude library
Summary(pl):	Statyczna biblioteka libprelude
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libprelude library.

%description static -l pl
Statyczna biblioteka libprelude.

%package -n perl-libprelude
Summary:	libprelude Perl bindings
Summary(pl):	Dowi±zania Perla do libprelude
Group:		Development/Languages/Perl

%description -n perl-libprelude
libprelude Perl bindings.

%description -n perl-libprelude -l pl
Dowi±zania Perla dla libprelude.

%package -n python-libprelude
Summary:	libprelude Python bindings
Summary(pl):	Dowi±zania Pythona dla libprelude
Group:		Development/Languages/Python

%description -n python-libprelude
libprelude Python bindings.

%description -n python-libprelude -l pl
Dowi±zania Pythona dla libprelude.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--enable-static \
	--enable-gtk-doc \
	--with-perl%{!?with_perl:=no} \
	--with-python%{!?with_python:=no} \
	--with-html-dir=%{_gtkdocdir}/libprelude

# first make the perl makefile otherwise with jobserver strange things happen:
# Makefile out-of-date with respect to Makefile.PL
%if %{with perl}
%{__make} -C bindings perl/Makefile
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with perl}
cd bindings/perl && %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
cd ../..
%{__make} -C bindings/perl install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_sysconfdir}/prelude
%dir %{_sysconfdir}/prelude/default
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prelude/default/*.conf
%dir %{_sysconfdir}/prelude/profile

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/prelude-adduser
%attr(755,root,root) %{_libdir}/lib*.so.*.*
# needed in normal operational
%{_libdir}/lib*.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libprelude-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libprelude
%{_aclocaldir}/*.m4
%{_gtkdocdir}/libprelude

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{with perl}
%files -n perl-libprelude
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/auto/Prelude
%attr(755,root,root) %{perl_vendorarch}/auto/Prelude/*.so
%{perl_vendorarch}/auto/Prelude/*.bs
%{perl_vendorarch}/Prelude.pm
%endif

%if %{with python}
%files -n python-libprelude
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%endif
