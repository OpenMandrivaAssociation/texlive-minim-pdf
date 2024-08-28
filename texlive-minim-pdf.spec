Name:		texlive-minim-pdf
Version:	70885
Release:	1
Summary:	Low-level PDF integration for LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minim-pdf
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-pdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-pdf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package adds low-level support to plain LuaTeX for marking
up the structure of a PDF document. The implementation is
rather basic, but should allow you to make your PDFs fully
PDF/A-compliant.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/minim-pdf
%doc %{_texmfdistdir}/doc/luatex/minim-pdf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
