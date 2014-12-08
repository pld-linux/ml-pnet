%define		pnetlib_version 0.8.0
Summary:	Extra C# libraries for pnet
Summary(pl.UTF-8):	Dodatkowe biblioteki C# dla pnet
Name:		ml-pnet
Version:	0.8.0
Release:	1
License:	LGPL
Vendor:		DotGNU
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
# Source0-md5:	b1c67faece957c23e6378cee50c0fdcb
URL:		http://www.gnu.org/software/dotgnu/pnet.html
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

%description -l pl.UTF-8
Ten pakiet zawiera kilka skryptów budujących używanych do budowania
klas bibliotek MONO i narzędzia używane z kompilatorem Portable.NET,
co pozwala użyć te biblioteki z środowiskiem Portable.NET.

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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/cscc/lib/*
