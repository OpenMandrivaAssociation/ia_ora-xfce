Summary:	Ia Ora Mandriva Xfce theme
Name:		ia_ora-xfce
Version:	1.0.2
Release:	10
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
Requires:	ia_ora-gnome-gtk2-engine
Requires:	ia_ora-gnome

%description
This is the Mandriva Ia Ora theme for the Xfce desktop environment.

%prep
%setup -q


%install
export datadir=%{_datadir}

%makeinstall_std

%files
%doc README ChangeLog
%{_datadir}/themes/*


%changelog
* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-8mdv2011.0
+ Revision: 653305
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-6mdv2009.1
+ Revision: 350286
- 2009.1 rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-5mdv2009.0
+ Revision: 247137
- rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix bug #38175

* Tue Feb 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 165666
- requires ia_ora-gnome

* Mon Jan 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2008.1
+ Revision: 146321
- ia_ora-xfce is now in mdv's svn
- new version
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 117758
- New release

  + Thierry Vignaud <tv@mandriva.org>
    - better description

* Fri Nov 23 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 111616
- import ia_ora-xfce


