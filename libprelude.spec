#
# Conditional build:
%bcond_without	lua	# Lua (5.1) bindings
%bcond_without	perl	# Perl bindings
%bcond_without	python	# Python bindings (required by prewikka)
%bcond_without	ruby	# Ruby bindings
#
%include	/usr/lib/rpm/macros.perl
Summary:	The Prelude library
Summary(pl.UTF-8):	Biblioteka Prelude
Name:		libprelude
Version:	1.0.1
Release:	13
License:	GPL v2 or commercial
Group:		Libraries
# https://www.prelude-ids.org/projects/prelude/files
Source0:	https://www.prelude-ids.org/attachments/download/241/%{name}-%{version}.tar.gz
# Source0-md5:	dce1ea9f82cf436830567894e7ee622f
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-ruby.patch
Patch2:		%{name}-gnutls.patch
Patch3:		%{name}-gets.patch
Patch4:		%{name}-python.patch
Patch5:		format-security.patch
Patch6:		python-install.patch
Patch7:		gcc5.patch
Patch8:		swig.patch
URL:		http://www.prelude-ids.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gnutls-devel >= 1.0.17
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libltdl-devel >= 2:2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.0
%{?with_lua:BuildRequires:	lua51-devel >= 5.1}
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python:BuildRequires:	python-devel >= 1:2.5}
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%{?with_ruby:BuildRequires:	ruby-devel >= 1.9}
BuildRequires:	sed >= 4.0
%{?with_perl:BuildRequires: swig-perl}
%{?with_python:BuildRequires: swig-python}
%{?with_ruby:BuildRequires: swig-ruby}
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
(obsługujące linię poleceń, linię konfiguracji i konfigurację dostępną
z zarządcy) oraz ogólne API wtyczek. Pozwala łatwo zamienić ulubiony
program związany z bezpieczeństwem na czujnik Prelude.

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

%package c++
Summary:	libpreludecpp - C++ binding for libprelude
Summary(pl.UTF-8):	libpreludecpp - wiązanie C++ do libprelude
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description c++
libpreludecpp - C++ binding for libprelude.

%description c++ -l pl.UTF-8
libpreludecpp - wiązanie C++ do libprelude.

%package c++-devel
Summary:	Header file for libpreludecpp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpreludecpp
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header file for libpreludecpp library - C++ binding for libprelude.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpreludecpp - wiązań C++ do libprelude.

%package c++-static
Summary:	Static libpreludecpp library
Summary(pl.UTF-8):	Statyczna biblioteka libpreludecpp
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static libpreludecpp library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka libpreludecpp.

%package -n lua-prelude
Summary:	PreludeEasy - libprelude Lua bindings
Summary(pl.UTF-8):	PreludeEasy - dowiązania języka Lua do libprelude
Group:		Development/Languages
Requires:	%{name}-c++ = %{version}-%{release}

%description -n lua-prelude
PreludeEasy - libprelude Lua bindings.

%description -n lua-prelude -l pl.UTF-8
PreludeEasy - dowiązania języka Lua do libprelude.

%package -n perl-libprelude
Summary:	Prelude Perl module - low-level Perl binding for libprelude
Summary(pl.UTF-8):	Moduł Perla Prelude - niskopoziomowe wiązanie Perla do libprelude
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}-%{release}

%description -n perl-libprelude
Prelude Perl module - low-level Perl binding for libprelude.

%description -n perl-libprelude -l pl.UTF-8
Moduł Perla Prelude - niskopoziomowe wiązanie Perla do libprelude.

%package -n perl-PreludeEasy
Summary:	PreludeEasy - high-level Perl binding for libprelude
Summary(pl.UTF-8):	PreludeEasy - wysokopoziomowe wiązanie Perla do libprelude
Group:		Development/Languages/Perl
Requires:	%{name}-c++ = %{version}-%{release}

%description -n perl-PreludeEasy
PreludeEasy - high-level Perl binding for libprelude.

%description -n perl-PreludeEasy -l pl.UTF-8
PreludeEasy - wysokopoziomowe wiązanie Perla do libprelude.

%package -n python-libprelude
Summary:	Low-level Python binding for libprelude
Summary(pl.UTF-8):	Niskopoziomowe wiązanie Pythona do libprelude
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-libprelude
Low-level Python binding for libprelude.

%description -n python-libprelude -l pl.UTF-8
Niskopoziomowe wiązanie Pythona do libprelude.

%package -n python-PreludeEasy
Summary:	PreludeEasy - high-level Python binding for libprelude
Summary(pl.UTF-8):	PreludeEasy - wysokopoziomowe wiązanie Pythona do libprelude
Group:		Development/Languages/Python
Requires:	%{name}-c++ = %{version}-%{release}

%description -n python-PreludeEasy
PreludeEasy - high-level Python binding for libprelude.

%description -n python-PreludeEasy -l pl.UTF-8
PreludeEasy - wysokopoziomowe wiązanie Pythona do libprelude.

%package -n ruby-prelude
Summary:	PreludeEasy - libprelude Ruby bindings
Summary(pl.UTF-8):	PreludeEasy - dowiązania języka Ruby do libprelude
Group:		Development/Languages
Requires:	%{name}-c++ = %{version}-%{release}

%description -n ruby-prelude
PreludeEasy - libprelude Ruby bindings.

%description -n ruby-prelude -l pl.UTF-8
PreludeEasy - dowiązania języka Ruby do libprelude.

%prep
%setup -q
%patch0 -p1

%if %{with python}
# regenerate with fresh swig for gcc 4.6+
%{__rm} bindings/python/{_PreludeEasy.cxx,PreludeEasy.py}
%endif
%if %{with ruby}
# same for ruby 1.9
%{__rm} bindings/ruby/PreludeEasy.cxx
%patch1 -p1
%endif
%if %{with perl}
# regenerate with fresh swig for perl 5.20
%{__rm} bindings/low-level/perl/Prelude.c
%endif

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

sed -i -e 's/lua >= 5.1/lua51 >= 5.1/' configure.in

%build
%{__libtoolize}
%{__aclocal} -I m4 -I libmissing/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	am_cv_ruby_rbexecdir=%{ruby_vendorarchdir} \
	--enable-gtk-doc \
	--enable-static \
	--with%{!?with_lua:out}-lua \
	--with%{!?with_perl:out}-perl \
	--with%{!?with_python:out}-python \
	--with-html-dir=%{_gtkdocdir}/libprelude \
	--with-perl-installdirs=vendor

%{__make}

cd bindings/perl
%{__make} clean
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C bindings/perl install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with lua}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/PreludeEasy.{la,a}
%endif
%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif
%if %{with ruby}
%{__rm} $RPM_BUILD_ROOT%{ruby_vendorarchdir}/PreludeEasy.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.README NEWS README
%attr(755,root,root) %{_bindir}/prelude-adduser
%attr(755,root,root) %{_bindir}/prelude-admin
%dir %{_sysconfdir}/prelude
%dir %{_sysconfdir}/prelude/default
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prelude/default/client.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prelude/default/global.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prelude/default/idmef-client.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prelude/default/tls.conf
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
%dir %{_includedir}/libprelude
%{_includedir}/libprelude/*.h
%{_aclocaldir}/libprelude.m4
%{_gtkdocdir}/libprelude
%{_pkgconfigdir}/libprelude.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libprelude.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpreludecpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpreludecpp.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpreludecpp.so
%{_libdir}/libpreludecpp.la
%{_includedir}/libprelude/idmef*.hxx
%{_includedir}/libprelude/prelude*.hxx

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libpreludecpp.a

%if %{with lua}
%files -n lua-prelude
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/PreludeEasy.so
%endif

%if %{with perl}
%files -n perl-libprelude
%defattr(644,root,root,755)
%{perl_vendorarch}/Prelude.pm
%dir %{perl_vendorarch}/auto/Prelude
%attr(755,root,root) %{perl_vendorarch}/auto/Prelude/Prelude.so

%files -n perl-PreludeEasy
%defattr(644,root,root,755)
%{perl_vendorarch}/PreludeEasy.pm
%dir %{perl_vendorarch}/auto/PreludeEasy
%attr(755,root,root) %{perl_vendorarch}/auto/PreludeEasy/PreludeEasy.so
%endif

%if %{with python}
%files -n python-libprelude
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_prelude.so
%{py_sitedir}/prelude.py[co]
%{py_sitedir}/prelude-%{version}-py*.egg-info

%files -n python-PreludeEasy
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_PreludeEasy.so
%{py_sitedir}/PreludeEasy.py[co]
%{py_sitedir}/PreludeEasy-%{version}-py*.egg-info
%endif

%if %{with ruby}
%files -n ruby-prelude
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/PreludeEasy.so
%endif
