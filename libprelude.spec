%include	/usr/lib/rpm/macros.perl
Summary:	The Prelude Library
Name:		libprelude
%define	_rc	rc9
Version:	0.9.0
Release:	0.%{_rc}.2
License:	GPL
Group:		Libraries
Source0:	http://www.prelude-ids.org/download/releases/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	924e4ccd0ca3bb57e16f9ead2a20d942
URL:		http://www.prelude-ids.org/
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	gtk-doc
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Prelude Library is a collection of generic functions providing
communication between the Prelude Hybrid IDS suite components. It
provides a convenient interface for sending alerts to Prelude Manager
with transparent SSL, failover and replication support, asynchronous
events and timer interfaces, an abstracted configuration API (hooking
at the commandline, the configuration line, or wide configuration,
available from the Manager), and a generic plugin API. It allows you
to easily turn your favorite security program into a Prelude sensor.

%package libs
Summary:	The Prelude Library
Group:		Development/Libraries

%description libs
The Prelude Library.

%package devel
Summary:	Header files and develpment documentation for libprelude
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gnutls-devel

%description devel
Header files and develpment documentation for libprelude.

%package static
Summary:	Static libprelude library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libprelude library.

%package -n perl-libprelude
Summary:	libprelude perl bindings
Group:		Development/Languages/Perl

%description -n perl-libprelude
libprelude perl bindings.

%package -n python-libprelude
Summary:	libprelude python bindings
Group:		Development/Languages/Python

%description -n python-libprelude
libprelude python bindings.

%prep
%setup -q -n %{name}-%{version}-%{_rc}

%build
%configure \
	--enable-shared \
	--enable-static \
	--enable-perl \
	--enable-python \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/libprelude

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd bindings/perl && %{__perl} Makefile.PL \
        INSTALLDIRS=vendor
cd ../..
%{__make} -C bindings/perl install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs   -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_sysconfdir}/prelude
%dir %{_sysconfdir}/prelude/default
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prelude/default/*.conf
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

%files -n perl-libprelude
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/auto/Prelude
%attr(755,root,root) %{perl_vendorarch}/auto/Prelude/*.so
%{perl_vendorarch}/auto/Prelude/*.bs
%{perl_vendorarch}/Prelude.pm

%files -n python-libprelude
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
 %{py_sitedir}/*.py[co]
