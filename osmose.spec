%define pkgname Osmose
%define pkgversion %(echo %version|sed s/\\\\\./-/g)

Name: osmose
Version: 0.9.2
Release: 1%{?dist}
Summary: A Sega Master System / Game Gear emulator

Group: Applications/Emulators
License: GPLv2+
URL: http://bcz.emu-france.com/%{name}.htm
Source: http://bcz.emu-france.com/%{name}/%{pkgname}-%{pkgversion}-src.zip
# Andrea Musuruane
Patch0: %{name}-0.9.2-usesystemlibraries.patch 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: SDL-devel
BuildRequires: minizip-devel
BuildRequires: mesa-libGL-devel

%description
Osmose is another Sega Master System / Gamegear emulator.


%prep
%setup -q -n %{pkgname}-%{pkgversion}
%patch0 -p1

# Make sure we don't use local zlib
rm -rf zlib

# Fix osmose on ppc
%ifarch ppc ppc64
sed -i 's/AUDIO_S16LSB/AUDIO_S16MSB/' OsmoseCore.cpp
%endif

# Fix end-of-line encoding
sed -i 's/\r//' *.txt *.{cpp,h} cpu/*.{cpp,h}

# Fix spurious executable permissions
chmod 644 cpu/*.{cpp,h}

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -D__USE_UNIX98"


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc changes.txt license.txt readme.txt



%changelog
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

