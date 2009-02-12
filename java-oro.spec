%bcond_without	javadoc		# don't build javadoc
Summary:	Full regular expressions API
Summary(pl.UTF-8):	Pełne API do wyrażeń regularnych
Name:		jakarta-oro
Version:	2.0.8
Release:	2
License:	Apache License
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/oro/%{name}-%{version}.zip
# Source0-md5:	af58ac4811ee023b6211446eb7b7fff2
Patch0:		%{name}-buildfix.patch
URL:		http://jakarta.apache.org/oro/
BuildRequires:	ant >= 1.5
BuildRequires:	java-gcj-compat-devel
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Jakarta-ORO Java classes are a set of text-processing Java classes
that provide Perl5 compatible regular expressions, AWK-like regular
expressions, glob expressions, and utility classes for performing
substitutions, splits, filtering filenames, etc. This library is the
successor to the OROMatcher, AwkTools, PerlTools, and TextTools
libraries from ORO, Inc. (http://www.oroinc.com/). They have been
donated to the Jakarta Project by Daniel Savarese
(http://www.savarese.org/), the copyright holder of the ORO libraries.
Daniel will continue to participate in their development under the
Jakarta Project.

%description -l pl.UTF-8
Klasy Javy Jakarta-ORO to zestaw klas do przetwarzania tekstu
udostępniający wyrażenia regularne zgodne z Perlem 5, awkowe wyrażenia
regularne, wyrażenia glob oraz klasy narzędziowe do wykonywania
podstawień, podziałów, filtrowania nazw plików itp. Ta biblioteka jest
następcą bibliotek OROMatcher, AwkTools, PerlTools i TextTools firmy
ORO Inc. (http://www.oroinc.com/). Zostały podarowane projektowi
Jakarta przez DAniela Savarese (http://www.savarese.org/), właściciela
praw autorskich do bibliotek ORO. Daniel będzie nadal udzielał się
przy rozwoju tych bibliotek w projekcie Jakarta.

%package javadoc
Summary:	Jakarta-ORO API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Jakarta-ORO
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Jakarta-ORO API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API biblioteki Jakarta-ORO.

%prep
%setup -q
%patch0 -p1

%build
unset CLASSPATH || :

%ant clean
%ant -Dfinal.name=oro -Dbuild.compiler=extJavac jar

%if %{with javadoc}
export SHELL=/bin/sh
%ant javadocs
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

cp oro.jar $RPM_BUILD_ROOT%{_javadir}/oro-%{version}.jar
ln -sf oro-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/oro.jar

cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc COMPILE ISSUES README TODO CHANGES CONTRIBUTORS LICENSE STYLE
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
