#
# Conditional build:
%bcond_without	lua		# Lua (5.1) bindings
%bcond_without	perl		# Perl bindings
%bcond_without	python2		# Python 2.x bindings (required by prewikka)
%bcond_without	python3		# Python 3.x bindings
%bcond_without	ruby		# Ruby bindings
%bcond_without	static_libs	# static libraries
#
# 5.1 also possible, 5.2 is preferred
%define	lua_ver	5.2
%define	lua_pkg	lua%(echo %{lua_ver} | tr -d .)
Summary:	The Prelude library
Summary(pl.UTF-8):	Biblioteka Prelude
Name:		libprelude
Version:	5.2.0
Release:	4
License:	GPL v2 or commercial
Group:		Libraries
#Source0Download: https://www.prelude-siem.org/projects/prelude/files
Source0:	https://www.prelude-siem.org/attachments/download/1395/%{name}-%{version}.tar.gz
# Source0-md5:	4db429af160450dc37c7ade001abf8c4
Patch0:		python-install.patch
Patch1:		%{name}-lua.patch
Patch2:		gtk-doc-1.32.patch
Patch3:		%{name}-cast.patch
Patch4:		%{name}-python.patch
URL:		https://www.prelude-siem.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gnulib >= 0-0.20181013.2
BuildRequires:	gnutls-devel >= 2.12.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libltdl-devel >= 2:2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.0
%{?with_lua:BuildRequires:	%{lua_pkg} >= %{lua_ver}}
%{?with_lua:BuildRequires:	%{lua_pkg}-devel >= %{lua_ver}}
BuildRequires:	pcre-devel
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python2:BuildRequires:	python-devel >= 1:2.5}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.745
%{?with_ruby:BuildRequires:	ruby-devel >= 1.9}
BuildRequires:	sed >= 4.0
%{?with_perl:BuildRequires: swig-perl >= 4.0.1}
%{?with_python:BuildRequires: swig-python >= 4.0.1}
%{?with_ruby:BuildRequires: swig-ruby >= 4.0.1}
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
Requires:	gnutls >= 2.12.0

%description libs
The Prelude library.

%description libs -l pl.UTF-8
Biblioteka Prelude.

%package devel
Summary:	Header files and development documentation for libprelude
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programistyczna dla libprelude
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnutls-devel >= 2.12.0
Requires:	libltdl-devel
Requires:	pcre-devel

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

%package swig
Summary:	SWIG development files for libprelude
Summary(pl.UTF-8):	Pliki programistyczne SWIG-a dla libprelude
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}
Requires:	swig

%description swig
SWIG development files for libprelude.

%description swig -l pl.UTF-8
Pliki programistyczne SWIG-a dla libprelude.

%package -n lua-prelude
Summary:	PreludeEasy - libprelude Lua bindings
Summary(pl.UTF-8):	PreludeEasy - dowiązania języka Lua do libprelude
Group:		Development/Languages
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{lua_pkg} >= %{lua_ver}

%description -n lua-prelude
PreludeEasy - libprelude Lua bindings.

%description -n lua-prelude -l pl.UTF-8
PreludeEasy - dowiązania języka Lua do libprelude.

%package -n perl-libprelude
Summary:	Prelude Perl module - Perl binding for libprelude
Summary(pl.UTF-8):	Moduł Perla Prelude - wiązanie Perla do libprelude
Group:		Development/Languages/Perl
Requires:	%{name}-c++ = %{version}-%{release}
Obsoletes:	perl-PreludeEasy < 1.2

%description -n perl-libprelude
Prelude Perl module - Perl binding for libprelude.

%description -n perl-libprelude -l pl.UTF-8
Moduł Perla Prelude - wiązanie Perla do libprelude.

%package -n python-libprelude
Summary:	Python 2.x binding for libprelude
Summary(pl.UTF-8):	Wiązanie Pythona 2.x do libprelude
Group:		Development/Languages/Python
Requires:	%{name}-c++ = %{version}-%{release}
Obsoletes:	python-PreludeEasy < 1.2

%description -n python-libprelude
Python 2.x binding for libprelude.

%description -n python-libprelude -l pl.UTF-8
Wiązanie Pythona 2.x do libprelude.

%package -n python3-libprelude
Summary:	Python 3.x binding for libprelude
Summary(pl.UTF-8):	Wiązanie Pythona 3.x do libprelude
Group:		Development/Languages/Python
Requires:	%{name}-c++ = %{version}-%{release}

%description -n python3-libprelude
Python 3.x binding for libprelude.

%description -n python3-libprelude -l pl.UTF-8
Wiązanie Pythona 3.x do libprelude.

%package -n ruby-prelude
Summary:	Ruby bindings for libprelude
Summary(pl.UTF-8):	Wiązania języka Ruby do libprelude
Group:		Development/Languages
Requires:	%{name}-c++ = %{version}-%{release}

%description -n ruby-prelude
Ruby bindings for libprelude.

%description -n ruby-prelude -l pl.UTF-8
Wiązania języka Ruby do libprelude.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

# in case swig regeneration is required:
#%{__rm} bindings/python/{_prelude.cxx,prelude.py}
# but note that the directory contains modified pystrings.swg from swig
# (4.0.1 as of libprelude 5.2.0), which might be incompatible with system swig
# (e.g. 4.0.x vs 4.2.x)

%build
gnulib-tool --copy-file lib/fseeko.c libmissing/fseeko.c
gnulib-tool --copy-file m4/fseeko.m4 libmissing/m4/fseeko.m4
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4 -I libmissing/m4
%{__autoconf}
%{__autoheader}
%{__automake}
# ac_cv_prog_HAVE_CXX=yes is a hack for some broken check
%configure \
	ac_cv_prog_HAVE_CXX=yes \
	am_cv_ruby_rbexecdir=%{ruby_vendorarchdir} \
	--enable-gtk-doc \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}/libprelude \
	--with-lua%{!?with_lua:=no} \
	--with-perl%{!?with_perl:=no} \
	--with-perl-installdirs=vendor \
	--with-python2%{!?with_python2:=no} \
	--with-python3%{!?with_python3:=no} \
	--with-swig

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitescriptdir} \
	pyexecdir=%{py_sitedir} \
	python3dir=%{py3_sitescriptdir} \
	py3execdir=%{py3_sitedir}

%if %{with lua}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lua/%{lua_ver}/prelude.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/lua/%{lua_ver}/prelude.a}
%endif
%if %{with python2}
%py_postclean
%endif
%if %{with ruby}
%{__rm} $RPM_BUILD_ROOT%{ruby_vendorarchdir}/Prelude.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{ruby_vendorarchdir}/Prelude.a}
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
%attr(755,root,root) %ghost %{_libdir}/libprelude.so.28

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
%{_mandir}/man1/libprelude-config.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libprelude.a
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpreludecpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpreludecpp.so.12

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpreludecpp.so
%{_libdir}/libpreludecpp.la
%{_includedir}/libprelude/idmef*.hxx
%{_includedir}/libprelude/prelude*.hxx

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libpreludecpp.a
%endif

%files swig
%defattr(644,root,root,755)
%dir %{_datadir}/libprelude
%{_datadir}/libprelude/swig

%if %{with lua}
%files -n lua-prelude
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lua/%{lua_ver}/prelude.so
%endif

%if %{with perl}
%files -n perl-libprelude
%defattr(644,root,root,755)
%{perl_vendorarch}/Prelude.pm
%dir %{perl_vendorarch}/auto/Prelude
%attr(755,root,root) %{perl_vendorarch}/auto/Prelude/Prelude.so
%endif

%if %{with python2}
%files -n python-libprelude
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_prelude.so
%{py_sitedir}/prelude.py[co]
%{py_sitedir}/prelude-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-libprelude
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/_prelude.cpython-*.so
%{py3_sitedir}/prelude.py
%{py3_sitedir}/__pycache__/prelude.cpython-*.py[co]
%{py3_sitedir}/prelude-%{version}-py*.egg-info
%endif

%if %{with ruby}
%files -n ruby-prelude
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/Prelude.so
%endif
