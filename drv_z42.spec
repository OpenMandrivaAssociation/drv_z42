Summary:	Printer driver for the Lexmark Z42, Z43 and Z52 printer
Name: 		drv_z42
Version:	0.4.3
Release:	21
License:	GPLv2
Group:		System/Printing
Url:		http://www.xs4all.nl/~pastolk/
Source:		http://www.xs4all.nl/~pastolk/%{name}-%{version}.tar.gz
Source1:	z42-2.png
Source2:	lexmark.png

BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gtk+-2.0)

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
%setup -qn %{name}

%build
pushd src
%{__cc} %{optflags} %{ldflags} -o z42_cmyk z42_cmyk.c
popd

pushd z42tool
%configure2_5x
%make
popd

%install
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

%files
%doc COPYING ChangeLog FAQ README
%{_bindir}/z42_cmyk

%files -n z42tool
%doc z42tool/README
%{_bindir}/z42tool
%{_datadir}/applications/*.desktop
%{_datadir}/z42tool
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
