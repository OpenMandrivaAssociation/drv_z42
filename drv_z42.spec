Summary:	Printer driver for the Lexmark Z42, Z43 and Z52 printer
Name: 		drv_z42
Version:	0.4.3
Release:	%mkrel 3
License:	GPL
Group:		System/Printing
URL:		http://www.xs4all.nl/~pastolk/
Source:		http://www.xs4all.nl/~pastolk/drv_z42-%{version}.tar.gz
BuildRequires:	X11-devel
BuildRequires:	xpm-devel
BuildRequires:	atk-devel
BuildRequires:	freetype2-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libfontconfig-devel
BuildRequires:	libz-devel
BuildRequires:	pango-devel
BuildRequires:	ImageMagick
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
%{__cc} %{optflags} -o z42_cmyk z42_cmyk.c
popd

pushd z42tool
%configure
%make
popd

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

pushd src
    install -m0755 z42_cmyk %{buildroot}%{_bindir}
popd

pushd z42tool
    %makeinstall
popd

# icon
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

convert z42tool/pixmaps/logo2.png -resize 16x16  %{buildroot}%{_miconsdir}/z42tool.png
convert z42tool/pixmaps/logo2.png -resize 32x32  %{buildroot}%{_iconsdir}/z42tool.png
convert z42tool/pixmaps/logo2.png -resize 48x48  %{buildroot}%{_liconsdir}/z42tool.png

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-z42tool.desktop << EOF
[Desktop Entry]
Name=z42tool - GUI for Lexmark printer maintence
Comment=GUI for Lexmark printer maintence
Exec=%{_bindir}/z42tool
Icon=z42tool
Terminal=false
Type=Application
Categories=System;Monitor;
EOF

%post -n z42tool
%update_menus

%postun -n z42tool
%clean_menus

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
