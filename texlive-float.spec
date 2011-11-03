# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/float
# catalog-date 2009-09-26 09:33:53 +0200
# catalog-license lppl
# catalog-version 1.3d
Name:		texlive-float
Version:	1.3d
Release:	1
Summary:	Improved interface for floating objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/float
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Improves the interface for defining floating objects such as
figures and tables. Introduces the boxed float, the ruled float
and the plaintop float. You can define your own floats and
improve the behaviour of the old ones. The package also
provides the H float modifier option of the obsolete here
package. You can select this as automatic default with
\floatplacement{figure}{H}.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/float/float.sty
%doc %{_texmfdistdir}/doc/latex/float/README
%doc %{_texmfdistdir}/doc/latex/float/float.pdf
#- source
%doc %{_texmfdistdir}/source/latex/float/float.dtx
%doc %{_texmfdistdir}/source/latex/float/float.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
