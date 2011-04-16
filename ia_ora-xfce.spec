Summary:	Ia Ora Mandriva Xfce theme
Name:		ia_ora-xfce
Version:	1.0.2
Release:	%mkrel 8
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
Requires:	ia_ora-gnome-gtk2-engine
Requires:	ia_ora-gnome
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the Mandriva Ia Ora theme for the Xfce desktop environment.

%prep
%setup -q


%install
rm -rf %{buildroot}
export datadir=%{_datadir}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_datadir}/themes/*
