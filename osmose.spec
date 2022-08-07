%define pkgname Osmose
%define pkgversion %(echo %version|sed s/\\\\\./-/g)

Name: osmose
Version: 0.9.96
Release: 21%{?dist}
Summary: A Sega Master System / Game Gear emulator

License: GPLv3+
URL: http://bcz.asterope.fr/
Source0: http://bcz.asterope.fr/%{name}/%{pkgname}-%{pkgversion}-QT.zip
Source1: %{name}.desktop
# Use system minizip
Patch0: %{name}-0.9.96-usesystemlibraries.patch 
# Fix building with gcc 4.7 
Patch1: %{name}-0.9.96-gcc47.patch

BuildRequires: gcc-c++
BuildRequires: qt4-devel
BuildRequires: alsa-lib-devel
%if 0%{?fedora} >= 30
BuildRequires: minizip-compat-devel
%else
BuildRequires: minizip-devel
%endif
BuildRequires: desktop-file-utils

%description
A multi-machine emulator for platforms of Sega consoles (Master System and 
Game Gear) and compatible for all games.

Simulates hardware extremely accurately which ensures that these classic 
games are represented exactly like they were on the real systems.

Osmose has a clean graphical user interface based on QT and a simplified 
setup process, and supports ROM archives in the SMS and GG formats.


%prep
%setup -q -n %{pkgname}-%{pkgversion}-QT
%patch0 -p1
%patch1 -p1

# Fix end-of-line encoding
sed -i 's/\r//' *.{cpp,h} cpu/*.{cpp,h}

# Fix spurious executable permissions
chmod 644 *.{cpp,h,txt} cpu/*.{cpp,h} osmose/*.{cpp,h} unzip/*.{c,h}

# Make sure we don't use local minizip
rm -rf unzip


%build
%qmake_qt4
%make_build


%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 755 %{pkgname}-%{pkgversion}-QT %{buildroot}%{_bindir}/%{name}

# Install desktop file
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files
%doc Readme.txt TODO.txt
%license License.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.96-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.96-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.96-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.96-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.96-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.96-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.96-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Andrea Musuruane <musuruan@gmail.com> - 0.9.96-14
- Added gcc dependency
- Updated BR to minizip-compat-devel for F30+

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.96-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.96-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.9.96-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 03 2017 Andrea Musuruane <musuruan@gmail.com> - 0.9.96-10
- Enabled debuginfo
- Dropped obsolete Group
- Dropped cleaning at the beginning of %%install
- Updated description

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.9.96-9
- Disable debuginfo
- Update spec file

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.96-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.96-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.9.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.96-5
- Mass rebuilt for Fedora 19 Features

* Sun Mar 18 2012 Andrea Musuruane <musuruan@gmail.com> - 0.9.96-4
- Fixed FTBFS for F17+

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.96-3
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 08 2011 Andrea Musuruane <musuruan@gmail.com> - 0.9.96-1
- New upstream release.
- New upstream URL and Source.
- Added desktop file to support new QT based GUI.
- Upstream changed license to GPLv3+.

* Sat Dec 12 2009 Andrea Musuruane <musuruan@gmail.com> - 0.9.2-1
- New upstream release.

* Sat Nov 07 2009 Andrea Musuruane <musuruan@gmail.com> - 0.9.1-1
- New upstream release.
- Removed no longer used patches.

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8.2-5
- rebuild for new F11 features

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.8.2-4
- rebuild for buildsys cflags issue

* Sat Feb 02 2008 Andrea Musuruane <musuruan@gmail.com> - 0.8.2-3
- Added a patch by Ian Chapman to compile with gcc 4.3.
- Timer timer patch has been updated by Ian to compile with gcc 4.3.

* Wed Jan 30 2008 Andrea Musuruane <musuruan@gmail.com> - 0.8.2-2
- Improved macro usage.
- Corrected License tag to reflect statement in main.cpp.
- Added patches by Ian Chapman to make osmose work on ppc.

* Sat Jan 19 2008 Andrea Musuruane <musuruan@gmail.com> - 0.8.2-1
- First release for Dribble/RPM Fusion.
- Made a patch to use system libraries and not to strip binary file.

