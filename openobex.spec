Summary:	Library for using OBEX
Summary(pl):	Biblioteka do obs³ugi protoko³u OBEX
Name:		openobex
Version:	1.0.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/openobex/%{name}-%{version}.tar.gz
# Source0-md5:	b845c760114027b6b7cad16a84963908
URL:		http://openobex.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library tries to implement a generic OBEX Session Protocol. It
does not implement the OBEX Application FrameWork.

%description -l pl
Ta biblioteka to próba implementacji podstawowego protoko³u sesji OBEX
Session Protocol. OBEX Application FrameWork nie jest
zaimplementowany.

%package devel
Summary:	Header files for Open OBEX
Summary(pl):	Pliki nag³ówkowe Open OBEX
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The header files are only needed for development of programs using the
Open OBEX library.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla
programistów u¿ywaj±cych biblioteki Open OBEX.

%package static
Summary:	Static Open OBEX library
Summary(pl):	Biblioteka statyczna Open OBEX
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Open OBEX library.

%description static -l pl
Biblioteka statyczna Open OBEX.

%package progs
Summary:	Open OBEX utility programs
Summary(pl):	Narzêdzia Open OBEX
Group:		Applications/Communications

%description progs
This package contains utility programs made to show Open OBEX library
usage.

%description progs -l pl
Ten pakiet zawiera narzêdzia zrobione aby pokazaæ sposób u¿ycia
biblioteki Open OBEX.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure

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
%attr(755,root,root) %{_libdir}/libopenobex-?.?.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenobex.so
%{_libdir}/libopenobex.la
%attr(755,root,root) %{_bindir}/openobex-config
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
