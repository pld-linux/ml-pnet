#
# Conditional build:
%bcond_without	tests	# "make check"
#
%define		pnetlib_version	0.8.0
Summary:	Mono Libraries for Portable.NET
Summary(pl.UTF-8):	Biblioteki Mono dla środowiska Portable.NET
Name:		ml-pnet
Version:	0.8.1
Release:	1
License:	GPL v2+ (pnet scripts), MIT/GPL v2 (Mono libraries/tools)
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
# Source0-md5:	0801c188d5a4ed8adea2c1479abe66ea
URL:		http://www.gnu.org/software/dotgnu/pnet.html
BuildRequires:	autoconf
BuildRequires:	automake
# required tools: ilrun csant ilgac ildd cscc
# required libraries: mscorlib Microsoft.VisualC
BuildRequires:	pnet-compiler-csharp = %{pnetlib_version}
BuildRequires:	pnet-ilinstall = %{pnetlib_version}
BuildRequires:	pnetlib-base = %{pnetlib_version}
BuildRequires:	pnetlib-winforms = %{pnetlib_version}
BuildRequires:	treecc
Requires:	pnetlib-base = %{pnetlib_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains a number of build scripts for building some
of the Mono class libraries and utility programs with Portable.NET's
C# compiler, so that they can be installed and used with
Portable.NET's runtime engine.

%description -l pl.UTF-8
Ten pakiet zawiera kilka skryptów budujących używanych do budowania
klas bibliotek i programów narzędziowych Mono przy użyciu kompilatora
C# Portable.NET. W ten sposób te komponenty Mono mogą być używane ze
środowiskiem Portable.NET.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake} --ignore-deps
%configure
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/nunit-console-pnet
%attr(755,root,root) %{_bindir}/sqlsharp-pnet
%attr(755,root,root) %{_bindir}/wsdl-pnet
%dir %{_libdir}/cscc/lib/0.7.6.1
%dir %{_libdir}/cscc/lib/1.0.0.0
%dir %{_libdir}/cscc/lib/1.0.5000.0
# %{_libdir}/cscc/lib/2.0.0.0 is in pnetlib-base
%dir %{_libdir}/cscc/lib/2.2.0.0

%{_libdir}/cscc/lib/0.7.6.1/ByteFX.Data.dll
%{_libdir}/cscc/lib/ByteFX.Data.dll

%{_libdir}/cscc/lib/1.0.0.0/IBM.Data.DB2.dll
%{_libdir}/cscc/lib/1.0.0.0/Mono.GetOptions.dll
%{_libdir}/cscc/lib/IBM.Data.DB2.dll
%{_libdir}/cscc/lib/Mono.GetOptions.dll

%{_libdir}/cscc/lib/1.0.5000.0/Mono.Cairo.dll
%{_libdir}/cscc/lib/1.0.5000.0/Mono.Data.SqliteClient.dll
%{_libdir}/cscc/lib/1.0.5000.0/Mono.Data.SybaseClient.dll
%{_libdir}/cscc/lib/1.0.5000.0/Mono.Data.Tds.dll
%{_libdir}/cscc/lib/1.0.5000.0/Mono.Data.TdsClient.dll
%{_libdir}/cscc/lib/1.0.5000.0/Mono.Http.dll
%{_libdir}/cscc/lib/1.0.5000.0/Mono.Security.dll
%{_libdir}/cscc/lib/1.0.5000.0/Novell.Directory.Ldap.dll
%{_libdir}/cscc/lib/1.0.5000.0/Npgsql.dll
%{_libdir}/cscc/lib/1.0.5000.0/PEAPI.dll
%{_libdir}/cscc/lib/Mono.Cairo.dll
%{_libdir}/cscc/lib/Mono.Data.SqliteClient.dll
%{_libdir}/cscc/lib/Mono.Data.SybaseClient.dll
%{_libdir}/cscc/lib/Mono.Data.Tds.dll
%{_libdir}/cscc/lib/Mono.Data.TdsClient.dll
%{_libdir}/cscc/lib/Mono.Http.dll
%{_libdir}/cscc/lib/Mono.Security.dll
%{_libdir}/cscc/lib/Novell.Directory.Ldap.dll
%{_libdir}/cscc/lib/Npgsql.dll
%{_libdir}/cscc/lib/PEAPI.dll

%attr(755,root,root) %{_libdir}/cscc/lib/2.0.0.0/sqlsharp-pnet.exe
%attr(755,root,root) %{_libdir}/cscc/lib/2.0.0.0/wsdl-pnet.exe
%attr(755,root,root) %{_libdir}/cscc/lib/sqlsharp-pnet.exe
%attr(755,root,root) %{_libdir}/cscc/lib/wsdl-pnet.exe

%{_libdir}/cscc/lib/2.0.0.0/Custommarshalers.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Data.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Data.OracleClient.dll
%{_libdir}/cscc/lib/2.0.0.0/System.DirectoryServices.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Management.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Messaging.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Runtime.Remoting.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Runtime.Serialization.Formatters.Soap.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Security.dll
%{_libdir}/cscc/lib/2.0.0.0/System.ServiceProcess.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Web.dll
%{_libdir}/cscc/lib/2.0.0.0/System.Web.Services.dll
%{_libdir}/cscc/lib/2.0.0.0/nunit.core.dll
%{_libdir}/cscc/lib/2.0.0.0/nunit.framework.dll
%{_libdir}/cscc/lib/2.0.0.0/nunit.util.dll
%{_libdir}/cscc/lib/Custommarshalers.dll
%{_libdir}/cscc/lib/System.Data.dll
%{_libdir}/cscc/lib/System.Data.OracleClient.dll
%{_libdir}/cscc/lib/System.DirectoryServices.dll
%{_libdir}/cscc/lib/System.Management.dll
%{_libdir}/cscc/lib/System.Messaging.dll
%{_libdir}/cscc/lib/System.Runtime.Remoting.dll
%{_libdir}/cscc/lib/System.Runtime.Serialization.Formatters.Soap.dll
%{_libdir}/cscc/lib/System.Security.dll
%{_libdir}/cscc/lib/System.ServiceProcess.dll
%{_libdir}/cscc/lib/System.Web.dll
%{_libdir}/cscc/lib/System.Web.Services.dll
%{_libdir}/cscc/lib/nunit.core.dll
%{_libdir}/cscc/lib/nunit.framework.dll
%{_libdir}/cscc/lib/nunit.util.dll

%attr(755,root,root) %{_libdir}/cscc/lib/2.2.0.0/nunit-console-pnet.exe
%attr(755,root,root) %{_libdir}/cscc/lib/nunit-console-pnet.exe
