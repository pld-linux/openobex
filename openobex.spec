#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for using OBEX
Summary(es.UTF-8):	Biblioteca para usar OBEX
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu OBEX
Name:		openobex
Version:	1.5
Release:	4
License:	LGPL v2.1+ (library), GPL v2+ (applications)
Group:		Libraries
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
# Source0-md5:	0d83dc86445a46a1b9750107ba7ab65c
Patch0:		%{name}-pc.patch
URL:		http://openobex.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	gettext-tools
BuildRequires:	libtool
BuildRequires:	libusb-compat-devel
BuildRequires:	pkgconfig
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
Requires:	libusb-compat-devel

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

%package apps
Summary:	Open OBEX utility programs
Summary(pl.UTF-8):	Narzędzia Open OBEX
License:	GPL v2+
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openobex-progs

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
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-apps \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libopenobex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenobex.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenobex.so
%{_libdir}/libopenobex.la
%{_includedir}/openobex
%{_pkgconfigdir}/openobex.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopenobex.a
%endif

%files apps
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ircp
%attr(755,root,root) %{_bindir}/irobex_palm3
%attr(755,root,root) %{_bindir}/irxfer
%attr(755,root,root) %{_bindir}/obex_tcp
%attr(755,root,root) %{_bindir}/obex_test
