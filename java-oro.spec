Summary:        Full regular expressions API
Summary(pl):	Pe³ne API do wyra¿eñ regularnych
Name:           jakarta-oro
Version:        2.0.7
Release:        0.1
License:        Apache License
Group:          Development/Languages/Java
Source0:        http://www.apache.org/dist/jakarta/oro/%{name}-%{version}.tar.gz
# Source0-md5:	5fdeff2f0386131027ad9ff282061dbf
URL:            http://jakarta.apache.org/oro/
BuildRequires:	jakarta-ant >= 1.5
Requires:	jre
Buildarch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

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

%description -l pl
Klasy Javy Jakarta-ORO to zestaw klas do przetwarzania tekstu
udostêpniaj±cy wyra¿enia regularne zgodne z Perlem 5, awkowe wyra¿enia
regularne, wyra¿enia glob oraz klasy narzêdziowe do wykonywania
podstawieñ, podzia³ów, filtrowania nazw plików itp. Ta biblioteka jest
nastêpc± bibliotek OROMatcher, AwkTools, PerlTools i TextTools firmy
ORO Inc. (http://www.oroinc.com/). Zosta³y podarowane projektowi
Jakarta przez DAniela Savarese (http://www.savarese.org/), w³a¶ciciela
praw autorskich do bibliotek ORO. Daniel bêdzie nadal udziela³ siê
przy rozwoju tych bibliotek w projekcie Jakarta.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
for file in `find . -type f -name .cvsignore`; do rm -rf $file; done

%build
ant -Dfinal.name=oro jar javadocs

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_javalibdir}
cp oro.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf oro.jar $RPM_BUILD_ROOT%{_javalibdir}/oro-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COMPILE ISSUES README TODO CHANGES CONTRIBUTORS LICENSE STYLE docs/api
%{_javadir}/*.jar
