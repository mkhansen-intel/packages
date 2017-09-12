Name:           test
Version:        1.0.0
Release:        1%{?dist}
Summary:        

License:        
URL:            https://github.com/mkhansen-intel/test
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  
Requires:       

%description


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install


%files
%doc



%changelog
* Sun Apr  3 2016 makerpm
-