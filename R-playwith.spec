%bcond_without bootstrap
%global packname  playwith
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9_53
Release:          1
Summary:          A GUI for interactive plots using GTK+
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-53.tar.gz
Requires:         R-lattice R-cairoDevice R-gWidgetsRGtk2 R-grid 
Requires:         R-RGtk2 R-gWidgets R-gridBase R-grDevices R-graphics R-stats R-utils 
%if %{with bootstrap}
Requires:         R-zoo R-MASS R-ggplot2 R-sp 
%else
Requires:         R-latticist R-zoo R-MASS R-ggplot2 R-sp 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lattice R-cairoDevice R-gWidgetsRGtk2 R-grid
BuildRequires:    R-RGtk2 R-gWidgets R-gridBase R-grDevices R-graphics R-stats R-utils 
%if %{with bootstrap}
BuildRequires:    R-zoo R-MASS R-ggplot2 R-sp 
%else
BuildRequires:    R-latticist R-zoo R-MASS R-ggplot2 R-sp 
%endif
BuildRequires:    x11-server-xvfb

%description
A GTK+ graphical user interface for editing and interacting with R plots.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
xvfb-run %{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
