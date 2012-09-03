# TODO
# - paths and deps for demo
%define		plugin	knob
Summary:	Nice, downward compatible, touchable, jQuery dial
Name:		jquery-%{plugin}
Version:	1.2.0
Release:	1
License:	MIT and GPL
Group:		Applications/WWW
Source0:	https://github.com/aterrien/jQuery-Knob/tarball/master/%{name}-%{version}.tgz
# Source0-md5:	acf069e9fd3ae21bdd7f77383b73cd42
URL:		http://anthonyterrien.com/knob/
BuildRequires:	closure-compiler
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	jquery >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery Knob:
- canvas based; no png or jpg sprites.
- touch, mouse and mousewheel, keyboard events implemented.
- downward compatible; overloads an input element.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qc
mv *-jQuery-Knob-*/* .

%build
install -d build/js

# compress .js
for js in js/*.js; do
	out=build/${js#*/jquery.}
%if 0%{!?debug:1}
	yuicompressor --charset UTF-8 $js -o $out
	js -C -f $out
%else
	cp -a $js $out
%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/%{plugin}.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p js/jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a index.html $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
