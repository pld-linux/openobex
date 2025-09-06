#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library for using OBEX
Summary(es.UTF-8):	Biblioteca para usar OBEX
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu OBEX
Name:		openobex
Version:	1.7.2
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (applications)
Group:		Libraries
Source0:	https://downloads.sourceforge.net/openobex/%{name}-%{version}-Source.tar.gz
# Source0-md5:	f6e0b6cb7dcfd731460a7e9a91429a3a
URL:		https://openobex.sourceforge.net/
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake >= 3.1
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	doxygen
BuildRequires:	gettext-tools
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library tries to implement a generic OBEX Session Protocol. It
does not implement the OBEX Application FrameWork.

%description -l es.UTF-8
Esta biblioteca procura dar una implementación genérica del protocolo
OBEX Session Protocol. La implementación de OBEX Application FrameWork
no está incluida.

%description -l pl.UTF-8
Ta biblioteka to próba implementacji podstawowego protokołu sesji OBEX
Session Protocol. OBEX Application FrameWork nie jest
zaimplementowany.

%package devel
Summary:	Header files for Open OBEX
Summary(es.UTF-8):	Ficheros de cabecera para Open OBEX
Summary(pl.UTF-8):	Pliki nagłówkowe Open OBEX
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bluez-libs-devel
Requires:	libusb-devel >= 1.0

%description devel
The header files are only needed for development of programs using the
Open OBEX library.

%description devel -l es.UTF-8
Estos ficheros de cabecera sólo son necesarios para desarrollar
programas que usan la biblioteca Open OBEX.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających biblioteki Open OBEX.

%package static
Summary:	Static Open OBEX library
Summary(es.UTF-8):	Biblioteca estática de Open OBEX
Summary(pl.UTF-8):	Biblioteka statyczna Open OBEX
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Open OBEX library.

%description static -l pl.UTF-8
Biblioteka statyczna Open OBEX.

%package apidocs
Summary:	Documentation for Open OBEX library
Summary(pl.UTF-8):	Dokumentacja biblioteki Open OBEX
Group:		Documentation
BuildArch:	noarch

%description apidocs
Documentation for Open OBEX library.

%description apidocs -l pl.UTF-8
Dokumentacja biblioteki Open OBEX.

%package apps
Summary:	Open OBEX utility programs
Summary(pl.UTF-8):	Narzędzia Open OBEX
License:	GPL v2+
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openobex-progs < 1.0

%description apps
This package contains utility programs made to show Open OBEX library
usage.

%description apps -l es.UTF-8
Este paquete contiene unas herramientas hechas para demonstrar el uso
de la biblioteca Open OBEX.

%description apps -l pl.UTF-8
Ten pakiet zawiera narzędzia zrobione aby pokazać sposób użycia
biblioteki Open OBEX.

%prep
%setup -q -n %{name}-%{version}-Source

# FIXME: better group?
%{__sed} -i -e 's/GROUP="plugdev"/GROUP="usb"/' udev/openobex.rules.in

%build
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_DOCUMENTATION=OFF \
	-DBUILD_SHARED_LIBS=OFF

%{__make}
cd ..
%endif

install -d build
cd build
%cmake ..

%{__make}

%{__make} openobex-apps

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_docdir}/html $RPM_BUILD_ROOT%{_docdir}/openobex-apidocs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/obex-check-device
%attr(755,root,root) %{_libdir}/libopenobex.so.*.*.*
%ghost %{_libdir}/libopenobex.so.2
/lib/udev/rules.d/60-openobex.rules

%files devel
%defattr(644,root,root,755)
%{_libdir}/libopenobex.so
%{_includedir}/openobex
%{_libdir}/cmake/OpenObex-%{version}
%{_pkgconfigdir}/openobex.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopenobex.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/openobex-apidocs

%files apps
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ircp
%attr(755,root,root) %{_bindir}/irobex_palm3
%attr(755,root,root) %{_bindir}/irxfer
%attr(755,root,root) %{_bindir}/obex_find
%attr(755,root,root) %{_bindir}/obex_tcp
%attr(755,root,root) %{_bindir}/obex_test
%{_mandir}/man1/ircp.1*
%{_mandir}/man1/irobex_palm3.1*
%{_mandir}/man1/irxfer.1*
%{_mandir}/man1/obex_find.1*
%{_mandir}/man1/obex_tcp.1*
%{_mandir}/man1/obex_test.1*
