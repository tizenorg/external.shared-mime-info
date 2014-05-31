Name:       shared-mime-info
Summary:    FreeDesktop.org shared MIME database and spec
Version:    0.60
Release:    13
Group:      misc
License:    GPLv2
Source0:    shared-mime-info-0.60.tar.gz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  intltool >= 0.35
BuildRequires:  libxml2

%description
FreeDesktop.org shared MIME database and spec
 This is the shared MIME-info database from the X Desktop Group. It is required
 by any program complying to the Shared MIME-Info Database spec, which is also
 included in this package.
 .
 At this time ROX and GNOME use this database. KDE is expected to follow soon, 
 and hopefully others too..

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
install  COPYING %{buildroot}/usr/share/license/%{name}

%files
%defattr(-,root,root,-)
/usr/bin/update-mime-database
/usr/share/*
%manifest shared-mime-info.manifest

%changelog
* Thu Jun 20 2013 - Hyungdeuk Kim <hd3.kim@samsung.com>
- Merge latest shared mime info(ver 1.1) related audio/aac

* Mon May 20 2013 - Hyungdeuk Kim <hd3.kim@samsung.com>
- Merge latest shared mime info(ver 1.1) related text/vcard
- Requested by s/w verification

* Wed May 8 2013 - Hyungdeuk Kim <hd3.kim@samsung.com>
- Add text/x-vnote mime type for .vnt files
- Requested by DCM

* Tue Apr 2 2013 - Hyungdek Kim <hd3.kim@samsung.com>
- Change ldp file mimetype to application/octet-stream
- Requested by media server

* Fri Jan 4 2013 - Hyungdeuk Kim <hd3.kim@samsung.com>
- Add audio/3gpp mime type for *.3ga files

* Wed Dec 26 2012 - Hyungdeuk Kim <hd3.kim@samsung.com>
- Add new mime type for supporting elm ext files
- Requested by email team
