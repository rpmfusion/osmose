%define pkgname Osmose
%define pkgversion %(echo %version|sed s/\\\\\./-/g)

Name: osmose
Version: 0.9.96
Release: 3%{?dist}
Summary: A Sega Master System / Game Gear emulator

Group: Applications/Emulators
License: GPLv3+
URL: http://bcz.asterope.fr/
Source0: http://bcz.asterope.fr/%{name}/%{pkgname}-%{pkgversion}-QT.zip
Source1: %{name}.desktop
# Use system minizip
Patch0: %{name}-0.9.96-usesystemlibraries.patch 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: qt4-devel
BuildRequires: alsa-lib-devel
BuildRequires: minizip-devel
BuildRequires: desktop-file-utils

%description
Osmose is another Sega Master System / Gamegear emulator.


%prep
%setup -q -n %{pkgname}-%{pkgversion}-QT
%patch0 -p1

# Fix end-of-line encoding
sed -i 's/\r//' *.{cpp,h} cpu/*.{cpp,h}

# Fix spurious executable permissions
chmod 644 *.{cpp,h,txt} cpu/*.{cpp,h} osmose/*.{cpp,h} unzip/*.{c,h}

# Make sure we don't use local minizip
rm -rf unzip


%build
export QMAKE_CFLAGS="%{optflags}"
export QMAKE_CXXFLAGS="%{optflags}"

qmake-qt4
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_bindir}
install -m 755 %{pkgname}-%{pkgversion}-QT %{buildroot}%{_bindir}/%{name}

# Install desktop file
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc License.txt Readme.txt TODO.txt


%changelog
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

