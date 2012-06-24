Summary:	Library for using OBEX
Summary(pl):	Biblioteka do obs�ugi protoko�u OBEX
Name:		openobex
Version:	0.9.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/openobex/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/openobex/%{name}-apps-%{version}.tar.gz
URL:		http://openobex.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library tries to implement a generic OBEX Session Protocol. It
does not implement the OBEX Application FrameWork.

%description -l pl
Ta biblioteka to pr�ba implementacji podstawowego protoko�u sesji OBEX
Session Protocol. OBEX Application FrameWork nie jest
zaimplementowany.

%package devel
Summary:	Header files for Open OBEX
Summary(pl):	Pliki nag��wkowe Open OBEX
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The header files are only needed for development of programs using the
Open OBEX library.

%description devel -l pl
W pakiecie tym znajduj� si� pliki nag��wkowe, przeznaczone dla
programist�w u�ywaj�cych biblioteki Open OBEX.

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
Summary(pl):	Narz�dzia Open OBEX
Group:		Applications/Communications

%description progs
This package contains utility programs made to show Open OBEX library
usage.

%description progs -l pl
Ten pakiet zawiera narz�dzia zrobione aby pokaza� spos�b u�ycia
biblioteki Open OBEX.

%prep
%setup -q -a1

%build
CFLAGS="%{rpmcflags}" \
./configure --prefix=%{_prefix}

${__make}

cd %{name}-apps-%{version}
ln -s ../src openobex

PATH="$PATH:.." \
CFLAGS="%{rpmcflags}" \
./configure --prefix=%{_prefix}

${__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

cd %{name}-apps-%{version}
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libopenobex-0.9.so.*.*

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

%files progs
%defattr(644,root,root,755)
%doc %{name}-apps-%{version}/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_bindir}/irobex_palm3
%attr(755,root,root) %{_bindir}/irxfer
%attr(755,root,root) %{_bindir}/obex_tcp
%attr(755,root,root) %{_bindir}/obex_test
