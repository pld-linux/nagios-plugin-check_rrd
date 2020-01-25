%define		plugin	check_rrd
Summary:	Nagios plugin to check values from RRD database
Name:		nagios-plugin-%{plugin}
Version:	1.0
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://exchange.nagios.org/components/com_mtree/attachment.php?link_id=489&cf_id=24#/%{plugin}.pl
# Source0-md5:	468e0b91c696b8b0278834ee0c2db516
Source1:	%{plugin}.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Databases/RRD/check_rrd-2Epl/details
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-tools-pod
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Generic Perl plugin to check age and values of an RRD database. It
uses RRDs and Nagios::Plugin.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}

%build
pod2man %{plugin} > %{plugin}.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir},%{_mandir}/man1}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg
cp -p %{plugin}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
%{_mandir}/man1/check_rrd.1*
