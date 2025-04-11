%global octpkg nan

Summary:	A statistics and machine learning toolbox for data with and w/o missing values
Name:		octave-nan
Version:	3.7.0
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/nan/
Source0:	https://downloads.sourceforge.net/octave/nan-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.4.1
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A statistics and machine learning toolbox for data with and w/o
missing values.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

