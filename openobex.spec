#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for using OBEX
Summary(es.UTF-8):	Biblioteca para usar OBEX
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu OBEX
Name:		openobex
Version:	1.3
Release:	5
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/openobex/%{name}-%{version}.tar.gz
# Source0-md5:	feaa5dfe5151c0e70e8f868fa4648a43
Patch0:		%{name}-link.patch
Patch1:		%{name}-pc.patch
URL:		http://openobex.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bluez-libs-devel
Requires:	libusb-devel

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
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Open OBEX library.

%description static -l pl.UTF-8
Biblioteka statyczna Open OBEX.

%package apps
Summary:	Open OBEX utility programs
Summary(pl.UTF-8):	Narzędzia Open OBEX
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
%patch0 -p1
%patch1 -p1

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
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libopenobex.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenobex.so
%{_libdir}/libopenobex.la
%{_includedir}/*
%{_aclocaldir}/*
%{_pkgconfigdir}/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%files apps
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ircp
%attr(755,root,root) %{_bindir}/irobex_palm3
%attr(755,root,root) %{_bindir}/irxfer
%attr(755,root,root) %{_bindir}/obex_tcp
%attr(755,root,root) %{_bindir}/obex_test
