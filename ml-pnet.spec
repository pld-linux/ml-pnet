Summary:	Extra C# libraries for pnet
Summary(pl):	Dodatkowe biblioteki C# dla pnet
Name:		ml-pnet
Version:	0.5.12
Release:	1
License:	LGPL
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	03a6db862c0fcec60ad89b8471eb8da3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pnet-compiler-csharp = %{version}
BuildRequires:	pnet-ilinstall = %{version}
BuildRequires:	pnetlib-base = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains a number of build scripts for building some
of the Mono class libraries and utility programs with Portable.NET's
C# compiler, so that they can be installed and used with
Portable.NET's runtime engine.

%description -l pl
Ten pakiet zawiera kilka skrypt�w buduj�cych u�ywanych do budowania
klas bibliotek MONO i narz�dzia u�ywane z kompilatorem Portable.NET,
co pozwala u�y� te biblioteki z �rodowiskiem Portable.NET.

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
