#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : evolution-data-server
Version  : 3.34.2
Release  : 61
URL      : https://download.gnome.org/sources/evolution-data-server/3.34/evolution-data-server-3.34.2.tar.xz
Source0  : https://download.gnome.org/sources/evolution-data-server/3.34/evolution-data-server-3.34.2.tar.xz
Summary  : Centralized access to appointments and contacts
Group    : Development/Tools
License  : LGPL-2.0
Requires: evolution-data-server-data = %{version}-%{release}
Requires: evolution-data-server-lib = %{version}-%{release}
Requires: evolution-data-server-libexec = %{version}-%{release}
Requires: evolution-data-server-license = %{version}-%{release}
Requires: evolution-data-server-locales = %{version}-%{release}
Requires: evolution-data-server-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : db-dev
BuildRequires : e2fsprogs-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : intltool
BuildRequires : liboauth-dev
BuildRequires : libsecret-dev
BuildRequires : libxml2-dev
BuildRequires : nss-dev
BuildRequires : openldap-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gcr-base-3)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gweather-3.0)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(krb5)
BuildRequires : pkgconfig(krb5-gssapi)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libical)
BuildRequires : pkgconfig(libical-glib)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsecret-unstable)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : python3
BuildRequires : sqlite-autoconf-dev
BuildRequires : usrbinpython
BuildRequires : webkitgtk-dev

%description
CAMEL

A generic Messaging Library
----

Introduction:
-------------
Camel is a generic messaging library. It supports the standard
messaging system for receiving and sending messages. It is the
messaging backend for Evolution.

%package data
Summary: data components for the evolution-data-server package.
Group: Data

%description data
data components for the evolution-data-server package.


%package dev
Summary: dev components for the evolution-data-server package.
Group: Development
Requires: evolution-data-server-lib = %{version}-%{release}
Requires: evolution-data-server-data = %{version}-%{release}
Provides: evolution-data-server-devel = %{version}-%{release}
Requires: evolution-data-server = %{version}-%{release}
Requires: evolution-data-server = %{version}-%{release}

%description dev
dev components for the evolution-data-server package.


%package lib
Summary: lib components for the evolution-data-server package.
Group: Libraries
Requires: evolution-data-server-data = %{version}-%{release}
Requires: evolution-data-server-libexec = %{version}-%{release}
Requires: evolution-data-server-license = %{version}-%{release}

%description lib
lib components for the evolution-data-server package.


%package libexec
Summary: libexec components for the evolution-data-server package.
Group: Default
Requires: evolution-data-server-license = %{version}-%{release}

%description libexec
libexec components for the evolution-data-server package.


%package license
Summary: license components for the evolution-data-server package.
Group: Default

%description license
license components for the evolution-data-server package.


%package locales
Summary: locales components for the evolution-data-server package.
Group: Default

%description locales
locales components for the evolution-data-server package.


%package services
Summary: services components for the evolution-data-server package.
Group: Systemd services

%description services
services components for the evolution-data-server package.


%prep
%setup -q -n evolution-data-server-3.34.2
cd %{_builddir}/evolution-data-server-3.34.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574442701
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%cmake .. -DENABLE_GOOGLE_AUTH=OFF  -DENABLE_UOA=OFF  -DENABLE_WEATHER=OFF -DWITH_LIBDB=OFF -DENABLE_INTROSPECTION=ON -DENABLE_VALA_BINDINGS=ON  -DENABLE_BACKEND_PER_PROCESS=ON -DENABLE_WEATHER=ON
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1574442701
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/evolution-data-server
cp %{_builddir}/evolution-data-server-3.34.2/COPYING %{buildroot}/usr/share/package-licenses/evolution-data-server/570d185ea721e7d6aee7426be1b10a800af98aa8
pushd clr-build
%make_install
popd
%find_lang evolution-data-server
## install_append content
mv %{buildroot}/usr/etc/xdg %{buildroot}/usr/share/xdg
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/camel-providers/libcamelimapx.urls
/usr/lib64/evolution-data-server/camel-providers/libcamellocal.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelnntp.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelpop3.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelsendmail.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelsmtp.urls

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Camel-1.2.typelib
/usr/lib64/girepository-1.0/EBackend-1.2.typelib
/usr/lib64/girepository-1.0/EBook-1.2.typelib
/usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
/usr/lib64/girepository-1.0/ECal-2.0.typelib
/usr/lib64/girepository-1.0/EDataBook-1.2.typelib
/usr/lib64/girepository-1.0/EDataCal-2.0.typelib
/usr/lib64/girepository-1.0/EDataServer-1.2.typelib
/usr/lib64/girepository-1.0/EDataServerUI-1.2.typelib
/usr/share/GConf/gsettings/evolution-data-server.convert
/usr/share/applications/org.gnome.Evolution-alarm-notify.desktop
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.Sources.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.UserPrompter.service
/usr/share/evolution-data-server/evolutionperson.schema
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.Evolution.DefaultSources.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.addressbook.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.calendar.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
/usr/share/pixmaps/evolution-data-server/category_birthday_16.png
/usr/share/pixmaps/evolution-data-server/category_business_16.png
/usr/share/pixmaps/evolution-data-server/category_favorites_16.png
/usr/share/pixmaps/evolution-data-server/category_gifts_16.png
/usr/share/pixmaps/evolution-data-server/category_goals_16.png
/usr/share/pixmaps/evolution-data-server/category_holiday-cards_16.png
/usr/share/pixmaps/evolution-data-server/category_holiday_16.png
/usr/share/pixmaps/evolution-data-server/category_hot-contacts_16.png
/usr/share/pixmaps/evolution-data-server/category_ideas_16.png
/usr/share/pixmaps/evolution-data-server/category_international_16.png
/usr/share/pixmaps/evolution-data-server/category_key-customer_16.png
/usr/share/pixmaps/evolution-data-server/category_miscellaneous_16.png
/usr/share/pixmaps/evolution-data-server/category_personal_16.png
/usr/share/pixmaps/evolution-data-server/category_phonecalls_16.png
/usr/share/pixmaps/evolution-data-server/category_status_16.png
/usr/share/pixmaps/evolution-data-server/category_strategies_16.png
/usr/share/pixmaps/evolution-data-server/category_suppliers_16.png
/usr/share/pixmaps/evolution-data-server/category_time-and-expenses_16.png
/usr/share/vala/vapi/camel-1.2.deps
/usr/share/vala/vapi/camel-1.2.vapi
/usr/share/vala/vapi/libebackend-1.2.deps
/usr/share/vala/vapi/libebackend-1.2.vapi
/usr/share/vala/vapi/libebook-1.2.deps
/usr/share/vala/vapi/libebook-1.2.vapi
/usr/share/vala/vapi/libebook-contacts-1.2.deps
/usr/share/vala/vapi/libebook-contacts-1.2.vapi
/usr/share/vala/vapi/libecal-2.0.deps
/usr/share/vala/vapi/libecal-2.0.vapi
/usr/share/vala/vapi/libedata-book-1.2.deps
/usr/share/vala/vapi/libedata-book-1.2.vapi
/usr/share/vala/vapi/libedata-cal-2.0.deps
/usr/share/vala/vapi/libedata-cal-2.0.vapi
/usr/share/vala/vapi/libedataserver-1.2.deps
/usr/share/vala/vapi/libedataserver-1.2.vapi
/usr/share/vala/vapi/libedataserverui-1.2.deps
/usr/share/vala/vapi/libedataserverui-1.2.vapi
/usr/share/xdg/autostart/org.gnome.Evolution-alarm-notify.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/evolution-data-server/camel/camel-address.h
/usr/include/evolution-data-server/camel/camel-async-closure.h
/usr/include/evolution-data-server/camel/camel-autocleanups.h
/usr/include/evolution-data-server/camel/camel-block-file.h
/usr/include/evolution-data-server/camel/camel-certdb.h
/usr/include/evolution-data-server/camel/camel-charset-map.h
/usr/include/evolution-data-server/camel/camel-cipher-context.h
/usr/include/evolution-data-server/camel/camel-data-cache.h
/usr/include/evolution-data-server/camel/camel-data-wrapper.h
/usr/include/evolution-data-server/camel/camel-db.h
/usr/include/evolution-data-server/camel/camel-debug.h
/usr/include/evolution-data-server/camel/camel-enums.h
/usr/include/evolution-data-server/camel/camel-enumtypes.h
/usr/include/evolution-data-server/camel/camel-file-utils.h
/usr/include/evolution-data-server/camel/camel-filter-driver.h
/usr/include/evolution-data-server/camel/camel-filter-input-stream.h
/usr/include/evolution-data-server/camel/camel-filter-output-stream.h
/usr/include/evolution-data-server/camel/camel-filter-search.h
/usr/include/evolution-data-server/camel/camel-folder-search.h
/usr/include/evolution-data-server/camel/camel-folder-summary.h
/usr/include/evolution-data-server/camel/camel-folder-thread.h
/usr/include/evolution-data-server/camel/camel-folder.h
/usr/include/evolution-data-server/camel/camel-gpg-context.h
/usr/include/evolution-data-server/camel/camel-html-parser.h
/usr/include/evolution-data-server/camel/camel-iconv.h
/usr/include/evolution-data-server/camel/camel-index.h
/usr/include/evolution-data-server/camel/camel-internet-address.h
/usr/include/evolution-data-server/camel/camel-junk-filter.h
/usr/include/evolution-data-server/camel/camel-local-settings.h
/usr/include/evolution-data-server/camel/camel-lock-client.h
/usr/include/evolution-data-server/camel/camel-lock-helper.h
/usr/include/evolution-data-server/camel/camel-lock.h
/usr/include/evolution-data-server/camel/camel-medium.h
/usr/include/evolution-data-server/camel/camel-memchunk.h
/usr/include/evolution-data-server/camel/camel-mempool.h
/usr/include/evolution-data-server/camel/camel-message-info-base.h
/usr/include/evolution-data-server/camel/camel-message-info.h
/usr/include/evolution-data-server/camel/camel-mime-filter-basic.h
/usr/include/evolution-data-server/camel/camel-mime-filter-bestenc.h
/usr/include/evolution-data-server/camel/camel-mime-filter-canon.h
/usr/include/evolution-data-server/camel/camel-mime-filter-charset.h
/usr/include/evolution-data-server/camel/camel-mime-filter-crlf.h
/usr/include/evolution-data-server/camel/camel-mime-filter-enriched.h
/usr/include/evolution-data-server/camel/camel-mime-filter-from.h
/usr/include/evolution-data-server/camel/camel-mime-filter-gzip.h
/usr/include/evolution-data-server/camel/camel-mime-filter-html.h
/usr/include/evolution-data-server/camel/camel-mime-filter-index.h
/usr/include/evolution-data-server/camel/camel-mime-filter-linewrap.h
/usr/include/evolution-data-server/camel/camel-mime-filter-pgp.h
/usr/include/evolution-data-server/camel/camel-mime-filter-progress.h
/usr/include/evolution-data-server/camel/camel-mime-filter-tohtml.h
/usr/include/evolution-data-server/camel/camel-mime-filter-windows.h
/usr/include/evolution-data-server/camel/camel-mime-filter-yenc.h
/usr/include/evolution-data-server/camel/camel-mime-filter.h
/usr/include/evolution-data-server/camel/camel-mime-message.h
/usr/include/evolution-data-server/camel/camel-mime-parser.h
/usr/include/evolution-data-server/camel/camel-mime-part-utils.h
/usr/include/evolution-data-server/camel/camel-mime-part.h
/usr/include/evolution-data-server/camel/camel-mime-utils.h
/usr/include/evolution-data-server/camel/camel-movemail.h
/usr/include/evolution-data-server/camel/camel-msgport.h
/usr/include/evolution-data-server/camel/camel-multipart-encrypted.h
/usr/include/evolution-data-server/camel/camel-multipart-signed.h
/usr/include/evolution-data-server/camel/camel-multipart.h
/usr/include/evolution-data-server/camel/camel-name-value-array.h
/usr/include/evolution-data-server/camel/camel-named-flags.h
/usr/include/evolution-data-server/camel/camel-net-utils.h
/usr/include/evolution-data-server/camel/camel-network-service.h
/usr/include/evolution-data-server/camel/camel-network-settings.h
/usr/include/evolution-data-server/camel/camel-nntp-address.h
/usr/include/evolution-data-server/camel/camel-null-output-stream.h
/usr/include/evolution-data-server/camel/camel-object-bag.h
/usr/include/evolution-data-server/camel/camel-object.h
/usr/include/evolution-data-server/camel/camel-offline-folder.h
/usr/include/evolution-data-server/camel/camel-offline-settings.h
/usr/include/evolution-data-server/camel/camel-offline-store.h
/usr/include/evolution-data-server/camel/camel-operation.h
/usr/include/evolution-data-server/camel/camel-partition-table.h
/usr/include/evolution-data-server/camel/camel-provider.h
/usr/include/evolution-data-server/camel/camel-sasl-anonymous.h
/usr/include/evolution-data-server/camel/camel-sasl-cram-md5.h
/usr/include/evolution-data-server/camel/camel-sasl-digest-md5.h
/usr/include/evolution-data-server/camel/camel-sasl-gssapi.h
/usr/include/evolution-data-server/camel/camel-sasl-login.h
/usr/include/evolution-data-server/camel/camel-sasl-ntlm.h
/usr/include/evolution-data-server/camel/camel-sasl-plain.h
/usr/include/evolution-data-server/camel/camel-sasl-popb4smtp.h
/usr/include/evolution-data-server/camel/camel-sasl-xoauth2-google.h
/usr/include/evolution-data-server/camel/camel-sasl-xoauth2-outlook.h
/usr/include/evolution-data-server/camel/camel-sasl-xoauth2.h
/usr/include/evolution-data-server/camel/camel-sasl.h
/usr/include/evolution-data-server/camel/camel-search-private.h
/usr/include/evolution-data-server/camel/camel-search-sql-sexp.h
/usr/include/evolution-data-server/camel/camel-service.h
/usr/include/evolution-data-server/camel/camel-session.h
/usr/include/evolution-data-server/camel/camel-settings.h
/usr/include/evolution-data-server/camel/camel-sexp.h
/usr/include/evolution-data-server/camel/camel-smime-context.h
/usr/include/evolution-data-server/camel/camel-store-settings.h
/usr/include/evolution-data-server/camel/camel-store-summary.h
/usr/include/evolution-data-server/camel/camel-store.h
/usr/include/evolution-data-server/camel/camel-stream-buffer.h
/usr/include/evolution-data-server/camel/camel-stream-filter.h
/usr/include/evolution-data-server/camel/camel-stream-fs.h
/usr/include/evolution-data-server/camel/camel-stream-mem.h
/usr/include/evolution-data-server/camel/camel-stream-null.h
/usr/include/evolution-data-server/camel/camel-stream-process.h
/usr/include/evolution-data-server/camel/camel-stream.h
/usr/include/evolution-data-server/camel/camel-string-utils.h
/usr/include/evolution-data-server/camel/camel-subscribable.h
/usr/include/evolution-data-server/camel/camel-text-index.h
/usr/include/evolution-data-server/camel/camel-transport.h
/usr/include/evolution-data-server/camel/camel-trie.h
/usr/include/evolution-data-server/camel/camel-uid-cache.h
/usr/include/evolution-data-server/camel/camel-url-scanner.h
/usr/include/evolution-data-server/camel/camel-url.h
/usr/include/evolution-data-server/camel/camel-utf8.h
/usr/include/evolution-data-server/camel/camel-utils.h
/usr/include/evolution-data-server/camel/camel-vee-data-cache.h
/usr/include/evolution-data-server/camel/camel-vee-folder.h
/usr/include/evolution-data-server/camel/camel-vee-message-info.h
/usr/include/evolution-data-server/camel/camel-vee-store.h
/usr/include/evolution-data-server/camel/camel-vee-summary.h
/usr/include/evolution-data-server/camel/camel-vtrash-folder.h
/usr/include/evolution-data-server/camel/camel-weak-ref-group.h
/usr/include/evolution-data-server/camel/camel.h
/usr/include/evolution-data-server/libebackend/e-backend-autocleanups.h
/usr/include/evolution-data-server/libebackend/e-backend-enums.h
/usr/include/evolution-data-server/libebackend/e-backend-enumtypes.h
/usr/include/evolution-data-server/libebackend/e-backend-factory.h
/usr/include/evolution-data-server/libebackend/e-backend.h
/usr/include/evolution-data-server/libebackend/e-cache-reaper.h
/usr/include/evolution-data-server/libebackend/e-cache.h
/usr/include/evolution-data-server/libebackend/e-collection-backend-factory.h
/usr/include/evolution-data-server/libebackend/e-collection-backend.h
/usr/include/evolution-data-server/libebackend/e-data-factory.h
/usr/include/evolution-data-server/libebackend/e-dbus-server.h
/usr/include/evolution-data-server/libebackend/e-file-cache.h
/usr/include/evolution-data-server/libebackend/e-oauth2-support.h
/usr/include/evolution-data-server/libebackend/e-offline-listener.h
/usr/include/evolution-data-server/libebackend/e-server-side-source-credentials-provider.h
/usr/include/evolution-data-server/libebackend/e-server-side-source.h
/usr/include/evolution-data-server/libebackend/e-source-registry-server.h
/usr/include/evolution-data-server/libebackend/e-sqlite3-vfs.h
/usr/include/evolution-data-server/libebackend/e-subprocess-factory.h
/usr/include/evolution-data-server/libebackend/e-user-prompter-server-extension.h
/usr/include/evolution-data-server/libebackend/e-user-prompter-server.h
/usr/include/evolution-data-server/libebackend/e-user-prompter.h
/usr/include/evolution-data-server/libebackend/e-webdav-collection-backend.h
/usr/include/evolution-data-server/libebackend/libebackend.h
/usr/include/evolution-data-server/libebook-contacts/e-address-western.h
/usr/include/evolution-data-server/libebook-contacts/e-book-contacts-enums.h
/usr/include/evolution-data-server/libebook-contacts/e-book-contacts-enumtypes.h
/usr/include/evolution-data-server/libebook-contacts/e-book-contacts-utils.h
/usr/include/evolution-data-server/libebook-contacts/e-book-query.h
/usr/include/evolution-data-server/libebook-contacts/e-contact.h
/usr/include/evolution-data-server/libebook-contacts/e-name-western.h
/usr/include/evolution-data-server/libebook-contacts/e-phone-number.h
/usr/include/evolution-data-server/libebook-contacts/e-source-backend-summary-setup.h
/usr/include/evolution-data-server/libebook-contacts/e-vcard.h
/usr/include/evolution-data-server/libebook-contacts/libebook-contacts.h
/usr/include/evolution-data-server/libebook/e-book-client-cursor.h
/usr/include/evolution-data-server/libebook/e-book-client-view.h
/usr/include/evolution-data-server/libebook/e-book-client.h
/usr/include/evolution-data-server/libebook/e-book-enumtypes.h
/usr/include/evolution-data-server/libebook/e-book-types.h
/usr/include/evolution-data-server/libebook/e-book-utils.h
/usr/include/evolution-data-server/libebook/e-book-view.h
/usr/include/evolution-data-server/libebook/e-book.h
/usr/include/evolution-data-server/libebook/e-destination.h
/usr/include/evolution-data-server/libebook/libebook.h
/usr/include/evolution-data-server/libecal/e-cal-check-timezones.h
/usr/include/evolution-data-server/libecal/e-cal-client-view.h
/usr/include/evolution-data-server/libecal/e-cal-client.h
/usr/include/evolution-data-server/libecal/e-cal-component-alarm-instance.h
/usr/include/evolution-data-server/libecal/e-cal-component-alarm-repeat.h
/usr/include/evolution-data-server/libecal/e-cal-component-alarm-trigger.h
/usr/include/evolution-data-server/libecal/e-cal-component-alarm.h
/usr/include/evolution-data-server/libecal/e-cal-component-alarms.h
/usr/include/evolution-data-server/libecal/e-cal-component-attendee.h
/usr/include/evolution-data-server/libecal/e-cal-component-datetime.h
/usr/include/evolution-data-server/libecal/e-cal-component-id.h
/usr/include/evolution-data-server/libecal/e-cal-component-organizer.h
/usr/include/evolution-data-server/libecal/e-cal-component-parameter-bag.h
/usr/include/evolution-data-server/libecal/e-cal-component-period.h
/usr/include/evolution-data-server/libecal/e-cal-component-property-bag.h
/usr/include/evolution-data-server/libecal/e-cal-component-range.h
/usr/include/evolution-data-server/libecal/e-cal-component-text.h
/usr/include/evolution-data-server/libecal/e-cal-component.h
/usr/include/evolution-data-server/libecal/e-cal-enums.h
/usr/include/evolution-data-server/libecal/e-cal-enumtypes.h
/usr/include/evolution-data-server/libecal/e-cal-recur.h
/usr/include/evolution-data-server/libecal/e-cal-system-timezone.h
/usr/include/evolution-data-server/libecal/e-cal-time-util.h
/usr/include/evolution-data-server/libecal/e-cal-util.h
/usr/include/evolution-data-server/libecal/e-reminder-watcher.h
/usr/include/evolution-data-server/libecal/e-timezone-cache.h
/usr/include/evolution-data-server/libecal/libecal.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-cache.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-factory.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-sexp.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-sqlitedb.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-summary.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-sync.h
/usr/include/evolution-data-server/libedata-book/e-book-backend.h
/usr/include/evolution-data-server/libedata-book/e-book-cache.h
/usr/include/evolution-data-server/libedata-book/e-book-meta-backend.h
/usr/include/evolution-data-server/libedata-book/e-book-sqlite.h
/usr/include/evolution-data-server/libedata-book/e-data-book-cursor-cache.h
/usr/include/evolution-data-server/libedata-book/e-data-book-cursor-sqlite.h
/usr/include/evolution-data-server/libedata-book/e-data-book-cursor.h
/usr/include/evolution-data-server/libedata-book/e-data-book-direct.h
/usr/include/evolution-data-server/libedata-book/e-data-book-factory.h
/usr/include/evolution-data-server/libedata-book/e-data-book-view.h
/usr/include/evolution-data-server/libedata-book/e-data-book.h
/usr/include/evolution-data-server/libedata-book/e-subprocess-book-factory.h
/usr/include/evolution-data-server/libedata-book/e-system-locale-watcher.h
/usr/include/evolution-data-server/libedata-book/libedata-book.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-factory.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-intervaltree.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-sexp.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-sync.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-util.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend.h
/usr/include/evolution-data-server/libedata-cal/e-cal-cache.h
/usr/include/evolution-data-server/libedata-cal/e-cal-meta-backend.h
/usr/include/evolution-data-server/libedata-cal/e-data-cal-factory.h
/usr/include/evolution-data-server/libedata-cal/e-data-cal-view.h
/usr/include/evolution-data-server/libedata-cal/e-data-cal.h
/usr/include/evolution-data-server/libedata-cal/e-subprocess-cal-factory.h
/usr/include/evolution-data-server/libedata-cal/libedata-cal.h
/usr/include/evolution-data-server/libedataserver/e-cancellable-locks.h
/usr/include/evolution-data-server/libedataserver/e-categories.h
/usr/include/evolution-data-server/libedataserver/e-client.h
/usr/include/evolution-data-server/libedataserver/e-collator.h
/usr/include/evolution-data-server/libedataserver/e-credentials.h
/usr/include/evolution-data-server/libedataserver/e-data-server-util.h
/usr/include/evolution-data-server/libedataserver/e-dataserver-autocleanups.h
/usr/include/evolution-data-server/libedataserver/e-debug-log.h
/usr/include/evolution-data-server/libedataserver/e-extensible.h
/usr/include/evolution-data-server/libedataserver/e-extension.h
/usr/include/evolution-data-server/libedataserver/e-flag.h
/usr/include/evolution-data-server/libedataserver/e-free-form-exp.h
/usr/include/evolution-data-server/libedataserver/e-gdata-oauth2-authorizer.h
/usr/include/evolution-data-server/libedataserver/e-iterator.h
/usr/include/evolution-data-server/libedataserver/e-list-iterator.h
/usr/include/evolution-data-server/libedataserver/e-list.h
/usr/include/evolution-data-server/libedataserver/e-memory.h
/usr/include/evolution-data-server/libedataserver/e-module.h
/usr/include/evolution-data-server/libedataserver/e-network-monitor.h
/usr/include/evolution-data-server/libedataserver/e-oauth2-service-base.h
/usr/include/evolution-data-server/libedataserver/e-oauth2-service-google.h
/usr/include/evolution-data-server/libedataserver/e-oauth2-service-outlook.h
/usr/include/evolution-data-server/libedataserver/e-oauth2-service.h
/usr/include/evolution-data-server/libedataserver/e-oauth2-services.h
/usr/include/evolution-data-server/libedataserver/e-operation-pool.h
/usr/include/evolution-data-server/libedataserver/e-proxy.h
/usr/include/evolution-data-server/libedataserver/e-secret-store.h
/usr/include/evolution-data-server/libedataserver/e-sexp.h
/usr/include/evolution-data-server/libedataserver/e-soup-auth-bearer.h
/usr/include/evolution-data-server/libedataserver/e-soup-session.h
/usr/include/evolution-data-server/libedataserver/e-soup-ssl-trust.h
/usr/include/evolution-data-server/libedataserver/e-source-address-book.h
/usr/include/evolution-data-server/libedataserver/e-source-alarms.h
/usr/include/evolution-data-server/libedataserver/e-source-authentication.h
/usr/include/evolution-data-server/libedataserver/e-source-autocomplete.h
/usr/include/evolution-data-server/libedataserver/e-source-autoconfig.h
/usr/include/evolution-data-server/libedataserver/e-source-backend.h
/usr/include/evolution-data-server/libedataserver/e-source-calendar.h
/usr/include/evolution-data-server/libedataserver/e-source-camel.h
/usr/include/evolution-data-server/libedataserver/e-source-collection.h
/usr/include/evolution-data-server/libedataserver/e-source-contacts.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider-impl-oauth2.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider-impl-password.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider-impl.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider.h
/usr/include/evolution-data-server/libedataserver/e-source-enums.h
/usr/include/evolution-data-server/libedataserver/e-source-enumtypes.h
/usr/include/evolution-data-server/libedataserver/e-source-extension.h
/usr/include/evolution-data-server/libedataserver/e-source-goa.h
/usr/include/evolution-data-server/libedataserver/e-source-ldap.h
/usr/include/evolution-data-server/libedataserver/e-source-local.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-account.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-composition.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-identity.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-signature.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-submission.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-transport.h
/usr/include/evolution-data-server/libedataserver/e-source-mdn.h
/usr/include/evolution-data-server/libedataserver/e-source-memo-list.h
/usr/include/evolution-data-server/libedataserver/e-source-offline.h
/usr/include/evolution-data-server/libedataserver/e-source-openpgp.h
/usr/include/evolution-data-server/libedataserver/e-source-proxy.h
/usr/include/evolution-data-server/libedataserver/e-source-refresh.h
/usr/include/evolution-data-server/libedataserver/e-source-registry-watcher.h
/usr/include/evolution-data-server/libedataserver/e-source-registry.h
/usr/include/evolution-data-server/libedataserver/e-source-resource.h
/usr/include/evolution-data-server/libedataserver/e-source-revision-guards.h
/usr/include/evolution-data-server/libedataserver/e-source-security.h
/usr/include/evolution-data-server/libedataserver/e-source-selectable.h
/usr/include/evolution-data-server/libedataserver/e-source-smime.h
/usr/include/evolution-data-server/libedataserver/e-source-task-list.h
/usr/include/evolution-data-server/libedataserver/e-source-uoa.h
/usr/include/evolution-data-server/libedataserver/e-source-weather.h
/usr/include/evolution-data-server/libedataserver/e-source-webdav.h
/usr/include/evolution-data-server/libedataserver/e-source.h
/usr/include/evolution-data-server/libedataserver/e-time-utils.h
/usr/include/evolution-data-server/libedataserver/e-uid.h
/usr/include/evolution-data-server/libedataserver/e-url.h
/usr/include/evolution-data-server/libedataserver/e-webdav-discover.h
/usr/include/evolution-data-server/libedataserver/e-webdav-session.h
/usr/include/evolution-data-server/libedataserver/e-xml-document.h
/usr/include/evolution-data-server/libedataserver/e-xml-hash-utils.h
/usr/include/evolution-data-server/libedataserver/e-xml-utils.h
/usr/include/evolution-data-server/libedataserver/eds-version.h
/usr/include/evolution-data-server/libedataserver/libedataserver.h
/usr/include/evolution-data-server/libedataserverui/e-cell-renderer-color.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter-impl-oauth2.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter-impl-password.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter-impl.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter.h
/usr/include/evolution-data-server/libedataserverui/e-reminders-widget.h
/usr/include/evolution-data-server/libedataserverui/e-trust-prompt.h
/usr/include/evolution-data-server/libedataserverui/e-webdav-discover-widget.h
/usr/include/evolution-data-server/libedataserverui/libedataserverui.h
/usr/lib64/libcamel-1.2.so
/usr/lib64/libebackend-1.2.so
/usr/lib64/libebook-1.2.so
/usr/lib64/libebook-contacts-1.2.so
/usr/lib64/libecal-2.0.so
/usr/lib64/libedata-book-1.2.so
/usr/lib64/libedata-cal-2.0.so
/usr/lib64/libedataserver-1.2.so
/usr/lib64/libedataserverui-1.2.so
/usr/lib64/pkgconfig/camel-1.2.pc
/usr/lib64/pkgconfig/evolution-data-server-1.2.pc
/usr/lib64/pkgconfig/libebackend-1.2.pc
/usr/lib64/pkgconfig/libebook-1.2.pc
/usr/lib64/pkgconfig/libebook-contacts-1.2.pc
/usr/lib64/pkgconfig/libecal-2.0.pc
/usr/lib64/pkgconfig/libedata-book-1.2.pc
/usr/lib64/pkgconfig/libedata-cal-2.0.pc
/usr/lib64/pkgconfig/libedataserver-1.2.pc
/usr/lib64/pkgconfig/libedataserverui-1.2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendcarddav.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendfile.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendgoogle.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendldap.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendcaldav.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendcontacts.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendfile.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendgtasks.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendhttp.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendweather.so
/usr/lib64/evolution-data-server/camel-providers/libcamelimapx.so
/usr/lib64/evolution-data-server/camel-providers/libcamellocal.so
/usr/lib64/evolution-data-server/camel-providers/libcamelnntp.so
/usr/lib64/evolution-data-server/camel-providers/libcamelpop3.so
/usr/lib64/evolution-data-server/camel-providers/libcamelsendmail.so
/usr/lib64/evolution-data-server/camel-providers/libcamelsmtp.so
/usr/lib64/evolution-data-server/credential-modules/module-credentials-goa.so
/usr/lib64/evolution-data-server/libedbus-private.so
/usr/lib64/evolution-data-server/registry-modules/module-cache-reaper.so
/usr/lib64/evolution-data-server/registry-modules/module-gnome-online-accounts.so
/usr/lib64/evolution-data-server/registry-modules/module-google-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-oauth2-services.so
/usr/lib64/evolution-data-server/registry-modules/module-outlook-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-secret-monitor.so
/usr/lib64/evolution-data-server/registry-modules/module-trust-prompt.so
/usr/lib64/evolution-data-server/registry-modules/module-webdav-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-yahoo-backend.so
/usr/lib64/libcamel-1.2.so.62
/usr/lib64/libcamel-1.2.so.62.0.0
/usr/lib64/libebackend-1.2.so.10
/usr/lib64/libebackend-1.2.so.10.0.0
/usr/lib64/libebook-1.2.so.20
/usr/lib64/libebook-1.2.so.20.1.3
/usr/lib64/libebook-contacts-1.2.so.3
/usr/lib64/libebook-contacts-1.2.so.3.0.0
/usr/lib64/libecal-2.0.so.1
/usr/lib64/libecal-2.0.so.1.0.0
/usr/lib64/libedata-book-1.2.so.26
/usr/lib64/libedata-book-1.2.so.26.0.0
/usr/lib64/libedata-cal-2.0.so.1
/usr/lib64/libedata-cal-2.0.so.1.0.0
/usr/lib64/libedataserver-1.2.so.24
/usr/lib64/libedataserver-1.2.so.24.0.0
/usr/lib64/libedataserverui-1.2.so.2
/usr/lib64/libedataserverui-1.2.so.2.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/camel-gpg-photo-saver
/usr/libexec/camel-index-control-1.2
/usr/libexec/camel-lock-helper-1.2
/usr/libexec/evolution-addressbook-factory
/usr/libexec/evolution-addressbook-factory-subprocess
/usr/libexec/evolution-calendar-factory
/usr/libexec/evolution-calendar-factory-subprocess
/usr/libexec/evolution-data-server/addressbook-export
/usr/libexec/evolution-data-server/csv2vcard
/usr/libexec/evolution-data-server/evolution-alarm-notify
/usr/libexec/evolution-data-server/list-sources
/usr/libexec/evolution-scan-gconf-tree-xml
/usr/libexec/evolution-source-registry
/usr/libexec/evolution-user-prompter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/evolution-data-server/570d185ea721e7d6aee7426be1b10a800af98aa8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/evolution-addressbook-factory.service
/usr/lib/systemd/user/evolution-calendar-factory.service
/usr/lib/systemd/user/evolution-source-registry.service
/usr/lib/systemd/user/evolution-user-prompter.service

%files locales -f evolution-data-server.lang
%defattr(-,root,root,-)

