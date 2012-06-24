#
# Conditional build:
%bcond_without	perl	# don't build perl bindings
%bcond_without	python	# don't build python bindings (required by prewikka)
#
%include	/usr/lib/rpm/macros.perl
Summary:	The Prelude library
Summary(pl.UTF-8):   Biblioteka Prelude
Name:		libprelude
Version:	0.9.12.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.prelude-ids.org/download/releases/%{name}-%{version}.tar.gz
# Source0-md5:	4636cf21c3e96adbd9463138fb49f401
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
Summary(pl.UTF-8):   Biblioteka Prelude
Group:		Libraries

%description libs
The Prelude library.

%description libs -l pl.UTF-8
Biblioteka Prelude.

%package devel
Summary:	Header files and development documentation for libprelude
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja programistyczna dla libprelude
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnutls-devel

%description devel
Header files and development documentation for libprelude.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programistyczna dla libprelude.

%package static
Summary:	Static libprelude library
Summary(pl.UTF-8):   Statyczna biblioteka libprelude
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libprelude library.

%description static -l pl.UTF-8
Statyczna biblioteka libprelude.

%package -n perl-libprelude
Summary:	libprelude Perl bindings
Summary(pl.UTF-8):   Dowiązania Perla do libprelude
Group:		Development/Languages/Perl

%description -n perl-libprelude
libprelude Perl bindings.

%description -n perl-libprelude -l pl.UTF-8
Dowiązania Perla dla libprelude.

%package -n python-libprelude
Summary:	libprelude Python bindings
Summary(pl.UTF-8):   Dowiązania Pythona dla libprelude
Group:		Development/Languages/Python

%description -n python-libprelude
libprelude Python bindings.

%description -n python-libprelude -l pl.UTF-8
Dowiązania Pythona dla libprelude.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--enable-static \
	--enable-gtk-doc \
	--with%{!?with_perl:out}-perl \
	--with%{!?with_python:out}-python \
	--with-html-dir=%{_gtkdocdir}/libprelude

# first make the perl makefile otherwise with jobserver strange things happen:
# Makefile out-of-date with respect to Makefile.PL
%if %{with perl}
%{__make} -C bindings perl/Makefile.PL
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libprelude-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
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
