// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-home",
          title: "Home",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/";
          },
        },{id: "nav-news",
          title: "News",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-members",
          title: "Members",
          description: "Members of the Interaction Lab",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "nav-publication",
          title: "Publication",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-activities",
          title: "Activities",
          description: "Learn how the crazy members of Interaction Lab play and study!",
          section: "Navigation",
          handler: () => {
            window.location.href = "/activities/";
          },
        },{id: "nav-teaching",
          title: "Teaching",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "post-one-paper-accepted-to-uist-2025-poster-track",
        
          title: "📄 One paper **accepted** to **UIST** 2025 **Poster** track!",
        
        description: "One paper accepted to UIST 2025 Poster track!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/one-paper-accepted-to-uist-2025-poster-track/";
          
        },
      },{id: "post-received-best-paper-honorable-mention-for-chi-2025-paper",
        
          title: "🏆 Received **Best Paper** **Honorable Mention** for **CHI**2025 paper!",
        
        description: "Received Best Paper Honorable Mention for CHI2025 paper!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/received-best-paper-honorable-mention-for-chi2025-paper/";
          
        },
      },{id: "post-received-best-paper-award-for-iui-2025-paper",
        
          title: "🏆 Received **Best Paper** **Award** for **IUI**2025 paper!",
        
        description: "Received Best Paper Award for IUI2025 paper!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/received-best-paper-award-for-iui2025-paper/";
          
        },
      },{id: "post-one-paper-accepted-to-2025-chi-lbw",
        
          title: "📄 One paper **accepted** to 2025 **CHI** **LBW**!",
        
        description: "One paper accepted to 2025 CHI LBW!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/one-paper-accepted-to-2025-chi-lbw/";
          
        },
      },{id: "post-two-papers-accepted-to-acm-chi-2025",
        
          title: "📄 Two papers **accepted** to **ACM** **CHI** 2025!",
        
        description: "Two papers accepted to ACM CHI 2025!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/two-papers-accepted-to-acm-chi-2025/";
          
        },
      },{id: "post-one-paper-accepted-to-acm-iui-2025",
        
          title: "📄 One paper **accepted** to **ACM** **IUI** 2025!",
        
        description: "One paper accepted to ACM IUI 2025!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/one-paper-accepted-to-acm-iui-2025/";
          
        },
      },{id: "post-one-paper-accepted-to-siggraph-asia-2024-as-poster",
        
          title: "📄 One paper **accepted** to **SIGGRAPH** ASIA 2024 as **poster**!",
        
        description: "One paper accepted to SIGGRAPH ASIA 2024 as poster!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/one-paper-accepted-to-siggraph-asia-2024-as-poster/";
          
        },
      },{id: "post-one-paper-accepted-to-ismar-2024",
        
          title: "📄 One paper **accepted** to **ISMAR** 2024!",
        
        description: "One paper accepted to ISMAR 2024!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/one-paper-accepted-to-ismar-2024/";
          
        },
      },{id: "post-our-paper-accepted-to-ijhci-if-4-7-21-9",
        
          title: "📄 Our paper **accepted** to IJHCI! (IF:4.7, 21.9%)",
        
        description: "Our paper accepted to IJHCI! (IF:4.7, 21.9%)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/our-paper-accepted-to-ijhci-if47-219/";
          
        },
      },{id: "post-our-paper-accepted-to-eait-if-5-5-6-9",
        
          title: "📄 Our paper **accepted** to EAIT! (IF:5.5, 6.9%)",
        
        description: "Our paper accepted to EAIT! (IF:5.5, 6.9%)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/our-paper-accepted-to-eait-if-55-69/";
          
        },
      },{id: "post-new-research-project-funded-by-wiset",
        
          title: "💰 New research **project** **funded** by **WISET**!",
        
        description: "New research project funded by WISET!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/new-research-project-funded-by-wiset/";
          
        },
      },{id: "post-one-paper-accepted-to-chi-2024-lbw",
        
          title: "📄 One paper **accepted** to **CHI** 2024 **LBW**!",
        
        description: "One paper accepted to CHI 2024 LBW!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/one-paper-accepted-to-chi-2024-lbw/";
          
        },
      },{id: "post-received-two-outstanding-papers-from-kcc-2023",
        
          title: "🏆 Received two **outstanding** papers from **KCC** 2023!",
        
        description: "Received two outstanding papers from KCC 2023!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/received-two-outstanding-papers-from-kcc-2023/";
          
        },
      },{id: "post-one-paper-accepted-to-mobilehci-2023",
        
          title: "📄 One paper **accepted** to **MobileHCI** 2023!",
        
        description: "One paper accepted to MobileHCI 2023!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/one-paper-accepted-to-mobilehci-2023/";
          
        },
      },{id: "post-one-paper-accepted-to-cvpr-workshop-abaw",
        
          title: "📄 One paper **accepted** to **CVPR** workshop! (**ABAW**)",
        
        description: "One paper accepted to CVPR workshop! (ABAW)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/one-paper-accepted-to-cvpr-workshop-abaw/";
          
        },
      },{id: "post-new-research-project-funded-by-wiset",
        
          title: "💰 New research **project** **funded** by **WISET**",
        
        description: "New research project funded by WISET",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/new-research-project-funded-by-wiset/";
          
        },
      },{id: "post-two-papers-accepted-to-2023-acm-chi-as-lbw",
        
          title: "📄 Two papers **accepted** to 2023 **ACM** **CHI** as **LBW**!",
        
        description: "Two papers accepted to 2023 ACM CHI as LBW!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/two-papers-accepted-to-2023-acm-chi-as-lbw/";
          
        },
      },{id: "post-new-research-grant-from-nrf",
        
          title: "💰 New research **grant** from **NRF**!",
        
        description: "New research grant from NRF!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/new-research-grant-from-nrf/";
          
        },
      },{id: "post-received-39-outstanding-technology-award-39-from-kird-competition",
        
          title: "🏆 Received &#39;**Outstanding** **Technology** **Award**&#39; from **KIRD** competition!",
        
        description: "Received &#39;Outstanding Technology Award&#39; from KIRD competition!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/received-outstanding-technology-award-from-kird-competition/";
          
        },
      },{id: "post-one-paper-accepted-to-eccv-workshop-on-affective-behavior-analysis-in-the-wild",
        
          title: "📄 One paper **accepted** to **ECCV** workshop on Affective Behavior Analysis in-the-wild!",
        
        description: "One paper accepted to ECCV workshop on Affective Behavior Analysis in-the-wild!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/one-paper-accepted-to-eccv-workshop-on-affective-behavior-analysis-in-the-wild/";
          
        },
      },{id: "post-received-two-outstanding-paper-award-s",
        
          title: "🏆 Received two **outstanding** paper **award**s!",
        
        description: "Received two outstanding paper awards!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/received-two-outstanding-paper-awards/";
          
        },
      },{id: "post-won-3rd-place-at-4th-abaw-competition-eccv-2022",
        
          title: "🏆 Won 3rd place at 4th **ABAW** competition! (**ECCV**2022)",
        
        description: "Won 3rd place at 4th ABAW competition! (ECCV2022)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/won-3rd-place-at-4th-abaw-competition-eccv2022/";
          
        },
      },{id: "post-new-funding-grant-ed-by-kird-real-challenge-2022-project",
        
          title: "💰 New funding **grant**ed by **KIRD** Real-Challenge 2022 **project**!",
        
        description: "New funding granted by KIRD Real-Challenge 2022 project!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/new-funding-granted-by-kird-real-challenge-2022-project/";
          
        },
      },{id: "post-one-paper-accepted-to-ieee-embc-2022",
        
          title: "📄 One paper **accepted** to **IEEE** EMBC 2022",
        
        description: "One paper accepted to IEEE EMBC 2022",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/one-paper-accepted-to-ieee-embc-2022/";
          
        },
      },{id: "post-one-paper-accepted-to-cancers-sci-if-6-639",
        
          title: "📄 One paper **accepted** to Cancers (SCI, IF:6.639)",
        
        description: "One paper accepted to Cancers (SCI, IF:6.639)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/one-paper-accepted-to-cancers-sci-if6639/";
          
        },
      },{id: "post-one-paper-accepted-to-cvpr-workshop-on-affective-behavior-analysis-in-the-wild",
        
          title: "📄 One paper **accepted** to **CVPR** workshop on Affective Behavior Analysis in-the-wild!",
        
        description: "One paper accepted to CVPR workshop on Affective Behavior Analysis in-the-wild!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/one-paper-accepted-to-cvpr-workshop-on-affective-behavior-analysis-in-the-wild/";
          
        },
      },{id: "post-won-2nd-place-at-abaw-2022",
        
          title: "🏆 Won 2nd place at **ABAW** 2022!",
        
        description: "Won 2nd place at ABAW 2022!",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/won-2nd-place-at-abaw-2022/";
          
        },
      },{id: "post-new-funding-grant-ed-by-wiset-2022-project",
        
          title: "💰 New funding **grant**ed by **WISET** 2022 **project**",
        
        description: "New funding granted by WISET 2022 project",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/new-funding-granted-by-wiset-2022-project/";
          
        },
      },{id: "post-one-paper-accepted-at-acm-etra-workshop-on-eye-tracking-in-learning-and-education",
        
          title: "📄 One paper **accepted** at **ACM** ETRA workshop on Eye-tracking in Learning and...",
        
        description: "One paper accepted at ACM ETRA workshop on Eye-tracking in Learning and Education",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/one-paper-accepted-at-acm-etra-workshop-on-eye-tra/";
          
        },
      },{id: "activities-2016-kcc",
          title: '2016 KCC',
          description: "Photos from 2016 KCC",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2016-kcc/";
            },},{id: "activities-2016-동계학회-참석",
          title: '2016 동계학회 참석',
          description: "Photos from 2016 Winter Conference Attendance",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2016-winter-conference/";
            },},{id: "activities-2017-edb-학회-참석",
          title: '2017 EDB 학회 참석',
          description: "Photos from 2017 EDB 학회 참석",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2017-edb/";
            },},{id: "activities-2017-nvidia-deep-learning-day",
          title: '2017 Nvidia Deep Learning Day',
          description: "Photos from 2017 Nvidia Deep Learning Day",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2017-nvidia-deep-learning-day/";
            },},{id: "activities-2018-ieee-embc",
          title: '2018 IEEE EMBC',
          description: "Photos from 2018 IEEE EMBC",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2018-ieee-embc/";
            },},{id: "activities-2018-정보기술학회-참석",
          title: '2018 정보기술학회 참석',
          description: "Photos from 2018 정보기술학회 참석",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2018/";
            },},{id: "activities-2019-acm-icmi",
          title: '2019 ACM ICMI',
          description: "Photos from 2019 ACM ICMI",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2019-acm-icmi/";
            },},{id: "activities-2019-ai-expo-amp-ai-korea",
          title: '2019 AI Expo &amp;amp; AI Korea',
          description: "Photos from 2019 AI Expo &amp; AI Korea",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2019-ai-expo-ai-korea/";
            },},{id: "activities-2019-ai-grand-challenge",
          title: '2019 AI Grand Challenge',
          description: "Photos from 2019 AI Grand Challenge",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2019-ai-grand-challenge/";
            },},{id: "activities-2019-iccv",
          title: '2019 ICCV',
          description: "Photos from 2019 ICCV",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2019-iccv/";
            },},{id: "activities-2019-kcc",
          title: '2019 KCC',
          description: "Photos from 2019 KCC",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2019-kcc/";
            },},{id: "activities-2019-nvidia-ai-conf",
          title: '2019 NVIDIA AI Conf',
          description: "Photos from 2019 NVIDIA AI Conf",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2019-nvidia-ai-conf/";
            },},{id: "activities-2021-aiexpo-seoultech",
          title: '2021 AIEXPO+SeoulTech',
          description: "Photos from 2021 AIEXPO+SeoulTech",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2021-aiexposeoultech/";
            },},{id: "activities-2021-esk",
          title: '2021 ESK',
          description: "Photos from 2021 ESK",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2021-esk/";
            },},{id: "activities-2021-kics",
          title: '2021 KICS',
          description: "Photos from 2021 KICS",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2021-kics/";
            },},{id: "activities-2022-cvpr",
          title: '2022 CVPR',
          description: "Photos from 2022 CVPR",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2022-cvpr/";
            },},{id: "activities-2022-embc",
          title: '2022 EMBC',
          description: "Photos from 2022 EMBC",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2022-embc/";
            },},{id: "activities-2022-esk",
          title: '2022 ESK',
          description: "Photos from 2022 ESK",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2022-esk/";
            },},{id: "activities-2022-kcc",
          title: '2022 KCC',
          description: "Photos from 2022 KCC",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2022-kcc/";
            },},{id: "activities-2022-smarttech",
          title: '2022 SmartTech',
          description: "Photos from 2022 SmartTech",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2022-smarttech/";
            },},{id: "activities-2022-workshop",
          title: '2022 Workshop',
          description: "Photos from 2022 Workshop",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2022-workshop/";
            },},{id: "activities-2023-chi",
          title: '2023 CHI',
          description: "Photos from 2023 CHI",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2023-chi/";
            },},{id: "activities-2023-hcik",
          title: '2023 HCIK',
          description: "Photos from 2023 HCIK",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2023-hcik/";
            },},{id: "activities-2023-kcc",
          title: '2023 KCC',
          description: "Photos from 2023 KCC",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2023-kcc/";
            },},{id: "activities-2023-kit-alumni-meeting",
          title: '2023 KIT Alumni Meeting',
          description: "Photos from 2023 KIT Alumni Meeting",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2023-kit-alumni-meeting/";
            },},{id: "activities-2023-summer-graduation",
          title: '2023 Summer Graduation',
          description: "Photos from 2023 Summer Graduation",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2023-summer-graduation/";
            },},{id: "activities-2024-chi",
          title: '2024 CHI',
          description: "Photos from 2024 CHI",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2024-chi/";
            },},{id: "activities-2024-esk",
          title: '2024 ESK',
          description: "Photos from 2024 ESK",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2024-esk/";
            },},{id: "activities-2024-graduation-amp-promotion",
          title: '2024 Graduation &amp;amp; Promotion',
          description: "Photos from 2024 Graduation &amp; Promotion",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2024-graduation-promotion/";
            },},{id: "activities-2024-hcik",
          title: '2024 HCIK',
          description: "Photos from 2024 HCIK",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2024-hcik/";
            },},{id: "activities-2024-ismar",
          title: '2024 ISMAR',
          description: "Photos from 2024 ISMAR",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2024-ismar/";
            },},{id: "activities-2024-siggraph-asia",
          title: '2024 SIGGRAPH ASIA',
          description: "Photos from 2024 SIGGRAPH ASIA",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2024-siggraph-asia/";
            },},{id: "activities-2025-bungjja",
          title: '2025 BungJJA!',
          description: "Photos from 2025 BungJJA!",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2025-bungjja/";
            },},{id: "activities-2025-chi",
          title: '2025 CHI',
          description: "Photos from 2025 CHI",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2025-chi/";
            },},{id: "activities-2025-hcik",
          title: '2025 HCIK',
          description: "Photos from 2025 HCIK",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2025-hcik/";
            },},{id: "activities-2025-home-coming",
          title: '2025 Home Coming',
          description: "Photos from 2025 Home Coming",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2025-home-coming/";
            },},{id: "activities-2025-iui",
          title: '2025 IUI',
          description: "Photos from 2025 IUI",
          section: "Activities",handler: () => {
              window.location.href = "/activities/2025-iui/";
            },},{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "news-a-simple-inline-announcement",
          title: 'A simple inline announcement.',
          description: "",
          section: "News",},{id: "news-a-long-announcement-with-details",
          title: 'A long announcement with details',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_2/";
            },},{id: "news-a-simple-inline-announcement-with-markdown-emoji-sparkles-smile",
          title: 'A simple inline announcement with Markdown emoji! :sparkles: :smile:',
          description: "",
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%79%6F%75@%65%78%61%6D%70%6C%65.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-inspire',
        title: 'Inspire HEP',
        section: 'Socials',
        handler: () => {
          window.open("https://inspirehep.net/authors/1010907", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=qc6CJjYAAAAJ", "_blank");
        },
      },{
        id: 'social-custom_social',
        title: 'Custom_social',
        section: 'Socials',
        handler: () => {
          window.open("https://www.alberteinstein.com/", "_blank");
        },
      },];
