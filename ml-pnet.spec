%define		pnetlib_version 0.6.4
Summary:	Extra C# libraries for pnet
Summary(pl):	Dodatkowe biblioteki C# dla pnet
Name:		ml-pnet
Version:	0.6.4
Release:	3
License:	LGPL
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	45151ac94ce2944f3348f42222b12f17
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pnet-compiler-csharp = %{version}
BuildRequires:	pnet-ilinstall = %{pnetlib_version}
BuildRequires:	pnetlib-base = %{pnetlib_version}
BuildRequires:	pnetlib-winforms = %{pnetlib_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains a number of build scripts for building some
of the Mono class libraries and utility programs with Portable.NET's
C# compiler, so that they can be installed and used with
Portable.NET's runtime engine.

%description -l pl
Ten pakiet zawiera kilka skryptów buduj±cych u¿ywanych do budowania
klas bibliotek MONO i narzêdzia u¿ywane z kompilatorem Portable.NET,
co pozwala u¿yæ te biblioteki z ¶rodowiskiem Portable.NET.

%prep
%setup -q

%build
%{__aclocal}
%{__automake} --ignore-deps
%{__autoconf}
%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/cscc/lib/*
