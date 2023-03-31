Name:		texlive-mcf2graph
Version:	64999
Release:	2
Summary:	Draw chemical structure diagrams with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mcf2graph
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcf2graph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcf2graph.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Molecular Coding Format (MCF) is a linear notation for
describing chemical structure diagrams. This package converts
MCF to graphic files using MetaPost.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/metapost/mcf2graph

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
