Summary:	Printer driver for the Lexmark Z42, Z43 and Z52 printer
Name: 		drv_z42
Version:	0.4.3
Release:	%mkrel 14
License:	GPL
Group:		System/Printing
URL:		http://www.xs4all.nl/~pastolk/
Source:		http://www.xs4all.nl/~pastolk/drv_z42-%{version}.tar.gz
Source1:	z42-2.png
Source2:        lexmark.png
BuildRequires:	gtk+2-devel
BuildRequires:	imagemagick
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Driver for the Lexmark printers Z42, Z43, Z52, X73 and the Compaq IJ1200.

%package -n	z42tool
Summary:	GUI for Lexmark printer maintence
Group:		System/Printing
Requires:	%{name} = %{version}

%description -n	z42tool
GUI tool to configure the Lexmark printers Z42, Z43, Z52, X73 and the Compaq
IJ1200.

%prep

%setup -q -n %{name}

%build
pushd src
%{__cc} %{optflags} %{ldflags} -o z42_cmyk z42_cmyk.c
popd

pushd z42tool
%configure2_5x
%make
popd

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

pushd src
    install -m0755 z42_cmyk %{buildroot}%{_bindir}
popd

pushd z42tool
    %makeinstall_std
popd

# icon
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

convert %SOURCE2 -resize 16x16  %{buildroot}%{_miconsdir}/z42tool.png
convert %SOURCE2 -resize 32x32  %{buildroot}%{_iconsdir}/z42tool.png
convert %SOURCE2 -resize 48x48  %{buildroot}%{_liconsdir}/z42tool.png

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-z42tool.desktop << EOF
[Desktop Entry]
Name=Lexmark printer manager
Comment=Status, alignment, cartridge maintenance
Exec=%{_bindir}/z42tool
Icon=z42tool
Terminal=false
Type=Application
Categories=System;Monitor;
EOF

%if %mdkversion < 200900
%post -n z42tool
%update_menus
%endif

%if %mdkversion < 200900
%postun -n z42tool
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING ChangeLog FAQ README
%attr(0755,root,root) %{_bindir}/z42_cmyk

%files -n z42tool
%defattr(0644,root,root,0755)
%doc z42tool/README
%{_datadir}/z42tool
%attr(0755,root,root) %{_bindir}/z42tool
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/*.desktop


%changelog
* Tue Jul 26 2011 Alex Burmashev <burmashev@mandriva.org> 0.4.3-13mdv2011.0
+ Revision: 691764
- changed default icon

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-12
+ Revision: 663883
- mass rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.4.3-11
+ Revision: 635314
- rebuild
- tighten BR

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-10mdv2011.0
+ Revision: 604830
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-9mdv2010.1
+ Revision: 518997
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-8mdv2010.0
+ Revision: 413407
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-7mdv2009.1
+ Revision: 318480
- use %%ldflags
- lowercase ImageMagick

  + Austin Acton <austin@mandriva.org>
    - simplify menu entry and unify with HP tool

* Thu Jun 26 2008 Austin Acton <austin@mandriva.org> 0.4.3-5mdv2009.0
+ Revision: 229185
- try to improve icon a bit (bug #36899)

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.4.3-4mdv2009.0
+ Revision: 218424
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-4mdv2008.1
+ Revision: 149678
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-3mdv2008.0
+ Revision: 75338
- fix deps (pixel)

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-2mdv2008.0
+ Revision: 64158
- use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-1mdv2008.0
+ Revision: 61472
- Import drv_z42



* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-1mdv2008.0
- initial Mandriva package

* Thu Jan 15 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-01-15 22:25:43 (44990)
- Added missing BuildRequires.

* Thu Jan 15 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-01-15 15:43:44 (44858)
- New upstream: 0.4.1
- Compiled against gtk+2
- Enabled parallel building

* Wed Mar 19 2003 Wanderlei Antonio Cavassin <cavassin@conectiva.com.br>
+ 2003-03-19 15:09:57 (28625)
- Rebuilt in new environment.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:33:47 (7661)
- Imported package from 8.0.
